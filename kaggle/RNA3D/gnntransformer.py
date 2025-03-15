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

from torch_geometric.data import Data
from torch_geometric.loader import DataLoader
from torch_geometric.nn import GATConv, global_mean_pool


class RNA3DTransformerGNN(nn.Module):

    def __init__(
            self, 
            in_channels: int,
            hidden_channels: int,
            nheads: int = 8,
            nlayers: int = 3,
            transformer_layers: int = 2,
            dropout: float = .2,
            device: str | None | device = None
    ) -> None:
        super().__init__()

        self.device = device if device is not None else torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self.convs = ModuleList()
        self.convs.append(
            GATConv(in_channels=in_channels, out_channels=hidden_channels, heads=nheads, dropout=dropout)
        )
        for _ in range(nlayers - 1):
            self.convs.append(
                GATConv(in_channels=hidden_channels * nheads, out_channels=hidden_channels, heads=nheads, dropout=dropout)
            )
        
        # Transformer Encoder Layer
        encoder_layer = TransformerEncoderLayer(d_model=hidden_channels * nheads, nhead=nheads, dropout=dropout)
        self.transformer_encoder = TransformerEncoder(encoder_layer=encoder_layer, num_layers=transformer_layers)

        # Final linear layer for coordinate prediction
        self.linear_pred = Linear(in_features=hidden_channels * nheads, out_features=3)  # out is the 3D coordinates
    
    def forward(self, x: Tensor, edge_index: Tensor, batch: Tensor) -> Tensor:

        for conv in self.convs:
            x = conv(x, edge_index)
            x = F.relu(x)
        
        batch_size = int(batch.max().item() + 1)
        seq_lens = torch.bincount(batch)
        max_len = int(seq_lens.max().item())

        x_padding = torch.zeros(size=(batch_size, max_len, x.size(-1)), device=self.device)  # [batch_size, seq_len, features]
        mask = torch.zeros(size=(batch_size, max_len), dtype=torch.bool, device=self.device)

        idx = 0
        for i, seq_len in enumerate(seq_lens):

            x_padding[i, :seq_len] = x[idx:idx + seq_len]
            mask[i, seq_len:] = True
            idx += seq_len
        
        x_padding = x_padding.transpose(0, 1)
        x_padding = self.transformer_encoder(x_padding, src_key_padding_mask=mask)
        x_padding = x_padding.transpose(0, 1)

        coords = self.linear_pred(x_padding)
        # coords_flat = torch.cat([coords[i, :seq_lens] for i in range(batch_size)], dim=0)
        # pooled_coords = global_mean_pool(coords_flat, batch)
        return coords

def main(dataList: List[Data]):

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Check if data is not empty and has valid x attribute
    if dataList and hasattr(dataList[0], 'x') and dataList[0].x is not None:
        in_channels = dataList[0].x.size(-1)
    else:
        raise ValueError("Input data must contain at least one element with valid features")

    data_loader = DataLoader(dataList, batch_size=8, shuffle=True)

    model = RNA3DTransformerGNN(
        in_channels=in_channels,
        hidden_channels=32,
        device=device,
    ).to(device=device)

    criterion = nn.MSELoss()
    optimizer = Adam(params=model.parameters(), lr=0.001)

    epoches = 100
    for epoch in range(epoches):
        
        model.train()
        loss = 0.0

        for loader in data_loader:
            data = loader.to(device=device)

            x, edge_indx, batch, y = data.x, data.edge_index, data.batch, data.y

            optimizer.zero_grad()

            coords = model(x, edge_indx, batch)
            seq_lens = torch.bincount(batch)
            coords_flat = []
            # start_idx = 0
            for i, seq_len in enumerate(seq_lens):
                coords_flat.append(coords[i, :int(seq_len)])
                # start_idx += seq_len
            coords_flat = torch.cat(coords_flat, dim=0)

            loss_ = criterion(coords_flat, y)
            loss_.backward()
            optimizer.step()

            loss += loss_.item() * data.num_graphs

        epoch_loss = loss / len(dataList)
        print(f"Epoch [{epoch}/{epoches}], Loss: {epoch_loss:.4f}")


if __name__ == '__main__':

    pass
