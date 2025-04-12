# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : main.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/29 16:04
# @Description:

from typing import Tuple

import random

import torch
from torch import Tensor, device
from torch.optim import Optimizer, AdamW
from torch.utils.data import random_split, Subset
from torch.optim.lr_scheduler import ReduceLROnPlateau

import torch_geometric.transforms as T
from torch_geometric.data import Dataset
from torch_geometric.loader import DataLoader
from sklearn.model_selection import train_test_split

from graphmodel import GPS
from pygdataset import RNA3DFolding

def load_dataset(root: str | None = None) -> Tuple[DataLoader, DataLoader]:
    
    if root is None:
        root = '/public/workspace/ryrl/IdeaProjects/Projects/torch/pyGenometrics/Cases/rna3d/'
    
    transform = T.AddRandomWalkPE(walk_length=20, attr_name='pe')
    datasets = RNA3DFolding(root, split='train', pre_transform=transform)

    indices = [i for i in range(len(datasets))]
    random.shuffle(indices)
    train_idx, test_idx = train_test_split(indices, train_size=.8)

    train_dataset = Subset(dataset=datasets, indices=train_idx)
    test_dataset = Subset(dataset=datasets, indices=test_idx)

    train_loader = DataLoader(train_dataset, shuffle=True, batch_size=16) # type: ignore
    val_loader = DataLoader(test_dataset, shuffle=False, batch_size=4) # type: ignore
    
    # val = RNA3DFolding(root, split='validation', pre_transform=transform)
    # train_loader = DataLoader(dataset=train, shuffle=True, batch_size=8)
    # val_loader = DataLoader(val, shuffle=False, batch_size=1)
    return train_loader, val_loader

def masked_loss(pred: Tensor, target: Tensor):

    masked = ~torch.isnan(target).any(dim=1)
    if masked.any():
        pred = pred[masked]
        target = target[masked]

        pred_center = pred.mean(dim=0, keepdim=True)
        target_center = target.mean(dim=0, keepdim=True)
        pred = pred - pred_center
        target = target - target_center

        H = pred.T @ target
        U, S, Vt = torch.linalg.svd(H)
        R = Vt.T @ U.T

        if torch.det(R) < 0:
            reflect = torch.eye(R.size(0), device=R.device, dtype=R.dtype)
            reflect[-1, -1] = -1.0
            R = R @ reflect

        pred_aligned = pred @ R
        rmsd = torch.sqrt(torch.mean((pred_aligned - target) ** 2))
        return rmsd
    else:
        return torch.tensor(0.0, device=pred.device, requires_grad=True)


def train(model:GPS, train_loader: DataLoader, optimizer: Optimizer, device: device | str):

    model.train()

    total_loss = 0
    for data in train_loader:
        data = data.to(device)
        optimizer.zero_grad()
        model.redraw_projection.redraw_projections()
        pred = model(data.x, data.pe, data.edge_index, data.edge_attr, data.batch)

        loss = masked_loss(pred, data.y)
        loss.backward()
        total_loss += loss.item() * data.num_graphs

        optimizer.step()
    return total_loss / len(train_loader.dataset)  # type: ignore

@torch.no_grad()
def test(model: GPS, loader: DataLoader, device: device | str):

    model.eval()
    
    total_error = 0
    for data in loader:
        data = data.to(device)

        pred = model(data.x, data.pe, data.edge_index, data.edge_attr, data.batch)
        total_error += masked_loss(pred, data.y).item() * data.num_graphs
    return total_error / len(loader.dataset)  # type: ignore

def run():

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    attn_kwargs = {'dropout': 0.5}
    # root = '/public/workspace/ryrl/IdeaProjects/Projects/torch/pyGenometrics/Cases/rna3d/'
    train_loader, val_loader = load_dataset()

    model = GPS(
        channels=128, pe_dim=32, num_layers=3, 
        attn_type='performer', attn_kwargs=attn_kwargs
    ).to(device)

    optimizer = AdamW(model.parameters(), lr=1e-4, weight_decay=1e-5)
    scheduler = ReduceLROnPlateau(optimizer=optimizer, mode='min', factor=.5, patience=20, min_lr=1e-6)

    # patience = 30  # Number of epochs to wait for improvement
    # min_delta = 0.0001  # Minimum change to qualify as improvement
    # patience_counter = 0
    # best_val_rmsd = float('inf')
    # best_model_path = '/public/workspace/ryrl/IdeaProjects/Projects/torch/pyGenometrics/Cases/rna3d/best_model.pt'

    for epoch in range(1, 1001):
        loss = train(model, train_loader, optimizer, device)
        val_rmsd = test(model, val_loader, device)

        scheduler.step(val_rmsd)
        print(f'Epoch: {epoch:02d}, Loss: {loss:.4f}, Val: {val_rmsd:.4f}')
    #     if val_rmsd < best_val_rmsd - min_delta:
    #         best_val_rmsd = val_rmsd
    #         patience_counter = 0
    #         # Save the best model
    #         torch.save(model.state_dict(), best_model_path)
    #         print(f"New best model saved with RMSD: {best_val_rmsd:.4f}")
    #     else:
    #         patience_counter += 1
    #         print(f"No improvement: {patience_counter}/{patience}")
            
    #     # Check if early stopping should be triggered
    #     if patience_counter >= patience:
    #         print(f"Early stopping triggered after {epoch} epochs")
    #         break
    
    # model.load_state_dict(torch.load(best_model_path))
    # print(f"Training complete. Best validation RMSD: {best_val_rmsd:.4f}")
    
    # Save final model (which is now the best model)
    torch.save(
        model.state_dict(), 
        '/public/workspace/ryrl/IdeaProjects/Projects/torch/pyGenometrics/Cases/rna3d/final_model.pt'
    )


if __name__ == '__main__':
    
    run()

    # root = '/public/workspace/ryrl/IdeaProjects/Projects/torch/pyGenometrics/Cases/rna3d/'
    # train_dataset = RNA3DFolding(root=root, split='train')
    # print(train_dataset)

    # model = GPS(
    #     channels=256, pe_dim=32, num_layers=7, 
    #     attn_type='performer', attn_kwargs={'dropout': 0.5}
    # )
    # print(model)

    # train_loader, val_loader = load_dataset()
    # for data in train_loader:
    #     print(data.pe)
