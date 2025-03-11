# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : gnntransformer.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/08 18:24
# @Description: 

from typing import Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F

from torch import Tensor, device
from torch.nn import Linear, ModuleList, TransformerEncoder, TransformerEncoderLayer

from torch_geometric.data import Data
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
    
    def forward(self, x: Tensor, edge_index: Tensor, batch: Tensor) -> Tuple[Tensor, Tensor]:

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
        coords_flat = torch.cat([coords[i, :seq_lens] for i in range(batch_size)], dim=0)
        pooled_coords = global_mean_pool(coords_flat, batch)
        return coords, pooled_coords


def nucleotide_encoder(nucleotide):
    mapping = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'U': [0, 0, 0, 1]}
    return mapping.get(nucleotide.upper(), [0, 0, 0, 0])

import pandas as pd

pd.Timestamp('2022-05-27')
pd.to_datetime('2022-05-27')

from scipy.spatial.distance import pdist, squareform