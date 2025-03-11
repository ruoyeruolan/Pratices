# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : preprocess.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/10 22:23
# @Description: 

import numpy as np
import pandas as pd

import torch
import torch.nn as nn
import torch.nn.functional as F

from scipy.spatial.distance import pdist, squareform

from torch_geometric.data import Data


def preprocess():
    train = pd.read_csv('./data/RNA3D/train_sequences.csv')
    dit = train.set_index('target_id').to_dict()
    
    labels = pd.read_csv('./data/RNA3D/train_labels.csv')
    labels['ID'] = labels['ID'].str.replace(r'_\d+$', '', regex=True)
    labels = labels.assign(**{str(key): labels['ID'].map(val) for key, val in dit.items()})
    labels = pd.concat([labels.iloc[:, 0], labels.iloc[:, 6], labels.iloc[:, 1:6], labels.iloc[:, 7:]], axis=1)
    labels['temporal_cutoff'] = labels['temporal_cutoff'].apply(pd.to_datetime)
    return labels

def create_rna_graph(
        data: pd.DataFrame, 
        use_spatial_distance:bool = True, 
        distance_threshold: float = 10.0, 
        embedding_dim: int = 64
):
    base_to_int = {'A': 0, 'C': 1, 'G': 2, 'U': 3, 'X': 4, '-': 4}
    num_bases = len(base_to_int)

    maxLength = data['resid'].max()
    embeddingLayer = nn.Embedding(maxLength + 1, embedding_dim=embedding_dim)

    # Apply vectorized operations
    bases = torch.tensor(data['resname'].map(base_to_int).values, dtype=torch.long)
    resids = torch.tensor(data['resid'].values, dtype=torch.long)

    base_one_hot = F.one_hot(bases, num_classes=num_bases).float()
    resid_embedding = embeddingLayer(resids)

    node_features = torch.cat([base_one_hot, resid_embedding], dim=1)
    
    num_nodes = data.shape[0]
    edges = []
    if use_spatial_distance and all(col in data.columns for col in ['x_1', 'y_1', 'z_1']):
        
        coords = data[['x_1', 'y_1', 'z_1']].values
        distances = squareform(pdist(coords))

        src, dst = np.where((
            distances < distance_threshold) & 
            (np.triu(np.ones_like(distances), k=1) > 0)
        )

        edges.extend(zip(src, dst))
        edges.extend(zip(dst, src))
        
    
    for i in range(num_nodes - 1):
        edges.append((i, i + 1))
        edges.append((i + 1, i))
    
    edges = list(set(edges))
    edge_index = torch.tensor(edges, dtype=torch.long).t().contiguous()
    
    graph_data = Data(x=node_features, edge_index=edge_index)
    graph_data.sequence = data['sequence'].iloc[0]
    graph_data.ID = data['ID'].iloc[0]
    return graph_data



if __name__ == '__main__':

    data = preprocess()

    