# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : gnntransformer.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/08 18:24
# @Description: 

from typing import Tuple, List

import torch
from torch import mode
import torch.nn as nn
import torch.nn.functional as F

from torch import Tensor, device
from torch.optim import Adam
from torch.nn import Linear, ModuleList, TransformerEncoder, TransformerEncoderLayer
from torch.optim.lr_scheduler import ReduceLROnPlateau

from torch_geometric.data import Data, Dataset, Batch
from torch_geometric.loader import DataLoader
from torch_geometric.nn import GATConv, global_mean_pool


# class RNA3DTransformerGNN(nn.Module):

#     def __init__(
#             self, 
#             in_channels: int,
#             hidden_channels: int,
#             nheads: int = 8,
#             nlayers: int = 3,
#             transformer_layers: int = 2,
#             dropout: float = .2,
#             device: str | None | device = None
#     ) -> None:
#         super().__init__()

#         self.device = device if device is not None else torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#         self.convs = ModuleList()
#         self.convs.append(
#             GATConv(in_channels=in_channels, out_channels=hidden_channels, heads=nheads, dropout=dropout)
#         )
#         for _ in range(nlayers - 1):
#             self.convs.append(
#                 GATConv(in_channels=hidden_channels * nheads, out_channels=hidden_channels, heads=nheads, dropout=dropout)
#             )
        
#         # Transformer Encoder Layer
#         encoder_layer = TransformerEncoderLayer(d_model=hidden_channels * nheads, nhead=nheads, dropout=dropout)
#         self.transformer_encoder = TransformerEncoder(encoder_layer=encoder_layer, num_layers=transformer_layers)

#         # Final linear layer for coordinate prediction
#         self.linear_pred = Linear(in_features=hidden_channels * nheads, out_features=3)  # out is the 3D coordinates
    
#     def forward(self, x: Tensor, edge_index: Tensor, batch: Tensor) -> Tensor:

#         for conv in self.convs:
#             x = conv(x, edge_index)
#             x = F.relu(x)
        
#         batch_size = int(batch.max().item() + 1)
#         seq_lens = torch.bincount(batch)
#         max_len = int(seq_lens.max().item())

#         x_padding = torch.zeros(size=(batch_size, max_len, x.size(-1)), device=self.device)  # [batch_size, seq_len, features]
#         mask = torch.zeros(size=(batch_size, max_len), dtype=torch.bool, device=self.device)

#         idx = 0
#         for i, seq_len in enumerate(seq_lens):

#             x_padding[i, :seq_len] = x[idx:idx + seq_len]
#             mask[i, seq_len:] = True
#             idx += seq_len
        
#         x_padding = x_padding.transpose(0, 1)
#         x_padding = self.transformer_encoder(x_padding, src_key_padding_mask=mask)
#         x_padding = x_padding.transpose(0, 1)

#         coords = self.linear_pred(x_padding)
#         coords_flat = torch.cat([coords[i, :seq_len] for i, seq_len in enumerate(seq_lens)], dim=0)
#         # pooled_coords = global_mean_pool(coords_flat, batch)
#         return coords_flat

class RNA3D(nn.Module):

    def __init__(
            self, 
            in_channels: int = 69, 
            hidden_channels: int = 128, 
            nlayers: int = 3,
            nheads: int = 8,
            dropout: float = .2,
    ) -> None:
        super().__init__()

        self.dropout = dropout

        self.convs = ModuleList()
        self.convs.append(
            GATConv(in_channels=in_channels, out_channels=hidden_channels, heads=nheads, dropout=dropout)
        )

        for _ in range(nlayers - 1):
            self.convs.append(
                GATConv(in_channels=hidden_channels * nheads, out_channels=hidden_channels, heads=nheads, dropout=dropout)
            )
        
        self.pred = Linear(in_features=hidden_channels * nheads, out_features=3)
    
    def forward(self, x: Tensor, edge_index: Tensor, batch: Tensor) -> Tensor:
        
        for idx in range(len(self.convs)):
            x = self.convs[idx](x, edge_index)

            if idx != len(self.convs) - 1:
                x = F.relu(x)
                x = F.dropout(x, p=self.dropout, training=self.training)
        return self.pred(x)

def masked_loss(criterion, output: Tensor, target: Tensor):

    if torch.isnan(target).any():
        mask = ~torch.isnan(target)
    
        output = output[mask]
        target = target[mask]

        if output.shape[0] == 0:
            return torch.tensor(0.0, requires_grad=True, device=output.device)
    return criterion(output, target)

class ListDataset(Dataset):

    def __init__(self, data_list):
        super().__init__()
        self.data_list = data_list
    
    def len(self):
        return len(self.data_list)
    
    def get(self, idx):
        return self.data_list[idx]

def train_single_graph(model, data_list, num_epochs=100, patience=5):

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)
    
    # 数据安全预处理
    def sanitize_data(data):
        with torch.no_grad():
            data.x = data.x.to(device).detach().clone().float().requires_grad_(False)
            data.edge_index = data.edge_index.to(device).detach().clone().long().requires_grad_(False)
            if hasattr(data, 'y'):
                data.y = data.y.to(device).detach().clone().float().requires_grad_(False)
                data.valid_mask = data.valid_mask.to(device).detach().clone().bool()
            return data
    
    valid_data = [sanitize_data(d) for d in data_list if (~torch.isnan(d.y)).any() if hasattr(d, 'y')]
    print(f"Training on {len(valid_data)}/{len(data_list)} valid graphs")

    train_loader = DataLoader(
        valid_data,
        batch_size=1,
        shuffle=True,
        num_workers=4,
        collate_fn=lambda batch: Batch.from_data_list(
            [sanitize_data(d) for d in batch],
            follow_batch=['sequence']
        )
    )

    optimizer = Adam(model.parameters(), lr=0.001)
    criterion = nn.MSELoss()
    

    for epoch in range(num_epochs):
        model.train()
        epoch_loss = 0.0
        valid_graphs = 0
        
        for batch in train_loader:
            assert not batch.x.requires_grad, "Input features contain gradients!"
            assert not batch.edge_index.requires_grad, "Edge indices contain gradients!"
            
            
            pred_coords = model(
                x=batch.x,
                edge_index=batch.edge_index,
                batch=batch.batch
            )
            
            valid_mask = batch.valid_mask if hasattr(batch, 'valid_mask') else ~torch.isnan(batch.y)
            loss = criterion(pred_coords[valid_mask], batch.y[valid_mask])
            
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            
            epoch_loss += loss.item()
            valid_graphs += 1

        # 日志输出
        avg_loss = epoch_loss / valid_graphs if valid_graphs > 0 else float('nan')
        print(f"Epoch {epoch+1:03d} | Train Loss: {avg_loss:.4f}")

    return model


