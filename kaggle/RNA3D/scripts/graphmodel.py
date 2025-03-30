# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : graph_model.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/23 18:54
# @Description: 

from typing import Dict, Any, Optional

import torch
import torch.nn as nn
from torch import Tensor

from torch_geometric.nn import GPSConv, GINEConv
from torch_geometric.nn.attention import PerformerAttention


class GPS(nn.Module):

    def __init__(self, channels: int, pe_dim: int, num_layers: int, attn_type: str, attn_kwargs: Dict[str, Any]):
        super().__init__()

        self.node_emb = nn.Embedding(num_embeddings=7, embedding_dim=channels - pe_dim)
        self.pe_lin = nn.Linear(in_features=20, out_features=pe_dim)
        self.pe_norm = nn.BatchNorm1d(num_features=20)
        self.edge_emb = nn.Embedding(num_embeddings=11, embedding_dim=channels)

        self.convs = nn.ModuleList()
        for _ in range(num_layers):
            pipeline = nn.Sequential(
                nn.Linear(channels, channels),
                nn.ReLU(),
                nn.Linear(channels, channels)
            )

            conv = GPSConv(
                channels=channels,
                conv=GINEConv(nn=pipeline),
                heads=4,
                attn_type=attn_type,
                attn_kwargs=attn_kwargs
            )

            self.convs.append(conv)
        
        self.mlp = nn.Sequential(
            nn.Linear(channels, channels // 2),
            nn.LayerNorm(channels // 2),
            nn.ReLU(),
            nn.Linear(channels // 2, channels // 4),
            nn.LayerNorm(channels // 4),
            nn.ReLU(),
            nn.Linear(channels // 4, 3)
        )

        self.redraw_projection = RedrawProjection(
            self.convs, 
            redraw_interval=1000 if attn_type == 'performer' else None
        )

    def forward(self, x: Tensor, pe, edge_index, edge_attr, batch):

        x_pe = self.pe_norm(pe)
        x = torch.cat((self.node_emb(x.squeeze(-1)), self.pe_lin(x_pe)), 1)
        edge_attr = self.edge_emb(edge_attr)

        for conv in self.convs:
            x = conv(x, edge_index, batch, edge_attr=edge_attr)
        # x = global_add_pool(x, batch)
        return self.mlp(x)

class RedrawProjection:

    def __init__(self, model: nn.Module, redraw_interval: Optional[int] = None):
        self.model = model
        self.redraw_interval = redraw_interval
        self.num_last_redraw = 0
    
    def redraw_projections(self):

        if not self.model.training or self.redraw_interval is None:
            return
        
        if self.num_last_redraw >= self.redraw_interval:
            fast_attentions = [
                module for module in self.model.modules() if isinstance(module, PerformerAttention)
            ]

            for fast_attention in fast_attentions:
                fast_attention.redraw_projection_matrix()
            self.num_last_redraw = 0
            return 
        self.num_last_redraw += 1