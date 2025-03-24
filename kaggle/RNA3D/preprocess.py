# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : preprocess.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/10 22:23
# @Description:


import bisect
import numpy as np
import pandas as pd
from tqdm import tqdm

from typing import List

import torch
import torch.nn as nn
import torch.nn.functional as F

from collections import defaultdict
from scipy.spatial.distance import pdist, squareform

from torch_geometric.data import Data
from torch_geometric.loader import DataLoader


def preprocess(fname: str = 'train'):
    train = pd.read_csv(f'./data/RNA3D/{fname}_sequences.csv')
    dit = train.set_index('target_id').to_dict()
    
    labels = pd.read_csv(f'./data/RNA3D/{fname}_labels.csv')
    labels['ID'] = labels['ID'].str.replace(r'_\d+$', '', regex=True)
    labels = labels.assign(**{str(key): labels['ID'].map(val) for key, val in dit.items()})
    labels = pd.concat([labels.iloc[:, 0], labels.iloc[:, 6], labels.iloc[:, 1:6], labels.iloc[:, 7:]], axis=1)
    labels['temporal_cutoff'] = labels['temporal_cutoff'].apply(pd.to_datetime)
    return labels

def pairing_rules(sequence: str, edges: list, nodes_number: list) -> list:
    pairs = {
        ('A','U'), ('U','A'),
        ('G','C'), ('C','G'),
        ('G','U'), ('U','G')
        }

    base_positions = defaultdict(list)
    for idx, base in enumerate(sequence):
        if idx in nodes_number:
            base_positions[base].append(idx)

    for (b1, b2) in pairs:
        list1_sorted = sorted(base_positions[b1])
        list2_sorted = sorted(base_positions[b2])

        for i in list1_sorted:
            pos = bisect.bisect_right(list2_sorted, i + 1)
            for j in list2_sorted[pos:]:
                edges.append((i, j))
                edges.append((j, i))
    return edges

def create_rna_graph(
        data: pd.DataFrame, 
        # use_spatial_distance: bool = True,
        use_pairing_rules: bool = True, 
        # distance_threshold: float = 12.0, 
        embedding_dim: int = 64
):
    base_to_int = {'A': 0, 'C': 1, 'G': 2, 'U': 3, 'X': 4, '-': 4}
    num_bases = 5

    num_nodes = maxLength = len(data['sequence'].iloc[0])
    embeddingLayer = nn.Embedding(maxLength + 1, embedding_dim=embedding_dim)

    # Apply vectorized operations
    bases = torch.tensor(data['resname'].map(base_to_int).values, dtype=torch.long)
    resids = torch.tensor(data['resid'].values, dtype=torch.long)

    base_one_hot = F.one_hot(bases, num_classes=num_bases).float()
    resid_embedding = embeddingLayer(resids)

    node_features = torch.cat([base_one_hot, resid_embedding], dim=1)
    
    edges = []
    nodes_number = data['resid'].to_list()
    for i in range(num_nodes - 1):
        if i in nodes_number and i + 1 in nodes_number:
            edges.append((i, i + 1))
            edges.append((i + 1, i))
    
    if use_pairing_rules:
        sequence = data['sequence'].iloc[0]
        edges = pairing_rules(sequence=sequence, edges=edges, nodes_number=nodes_number)
        
    edges = list(set(edges))
    edge_index = torch.tensor(edges, dtype=torch.long).t().contiguous()
    
    graph_data = Data(x=node_features, edge_index=edge_index)

    if 'x_1' in data.columns:
        graph_data.y = torch.tensor(data[['x_1', 'y_1', 'z_1']].values, dtype=torch.float)

    graph_data.sequence = sequence
    graph_data.ID = data['ID'].iloc[0]
    return graph_data



if __name__ == '__main__':

    data = preprocess()
    df = data.groupby(by='ID')
    graph_list = [create_rna_graph(data=group) for _, group in tqdm(df, total=len(df))]

    train_loader = DataLoader(graph_list, batch_size=8, shuffle=True)
