# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : pygdataset.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/20 19:29
# @Description: 

import os
import os.path as osp

from tqdm import tqdm

from typing import Callable, Any, List
from collections import defaultdict

import bisect
import pandas as pd
import polars as pl

import torch
import torch.nn as nn
import torch.nn.functional as F

from torch_geometric.io import fs
from torch_geometric.data import Data, InMemoryDataset
from torch_geometric.data import Dataset, download_url, extract_zip


class RNA3DFolding(InMemoryDataset):

    url = 'https://www.kaggle.com/competitions/87793/download-all'

    def __init__(
            self, 
            root: str | None = None, 
            split: str | None = None,
            transform: Callable[..., Any] | None = None, 
            pre_transform: Callable[..., Any] | None = None, 
            pre_filter: Callable[..., Any] | None = None, 
            log: bool = True, 
            force_reload: bool = False
    ) -> None:
        assert split in ['train', 'test', 'val']
        super().__init__(
            root, transform, pre_transform, 
            pre_filter, force_reload=force_reload, log=log
        )

        path = osp.join(self.processed_dir, f'{split}.pt')
    
    @property
    def raw_file_name(self) -> List[str]:
        return [
            'test_sequences.csv',
            'train_sequences.csv', 'train_labels.csv',
            'validation_sequences.csv', 'validation_labels.csv'
        ]
    
    @property
    def processed_dir(self) -> str:
        return osp.join(self.root, 'full', 'processed')
    
    @property
    def processed_file_name(self) -> List[str]:
        return ['train.pt', 'test.pt', 'val.pt']
    
    def download(self) -> None:
        fs.rm(self.raw_dir)
        path = download_url(self.url, self.root)
        extract_zip(path=path, folder=self.root)
        os.rename(osp.join(self.root, 'stanford-rna-3d-folding'), self.raw_dir)
        os.unlink(path)
    
    def preprocess(self, fname: str = 'train') -> pd.DataFrame:

        seq = pd.read_csv(osp.join(self.raw_dir, fname, '_sequences.csv'))
        seq['temporal_cutoff'] = seq['temporal_cutoff'].apply(pd.to_datetime)
        dit = seq.set_index('target_id').to_dict()

        labels = pd.read_csv(osp.join(self.raw_dir, fname, '_labels.csv'))
        labels['ID'] = labels['ID'].str.replace(r'_\d+$', '', regex=True)
        labels = labels.assign(**{str(key): labels['ID'].map(val) for key, val in dit.items()})

        if fname == 'train':
            cutoff = pd.Timestamp('2022-05-27')
            labels = labels.query(f'temporal_cutoff < {cutoff}')
        return labels
    
    def pairing_rules(
            self, 
            sequence: str, 
            edges: list, 
            nodes_number: list
    ) -> list:
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
            self,
            data: pd.DataFrame, 
            use_pairing_rules: bool = True, 
            embedding_dim: int = 64
):
        base_to_int = {'A': 0, 'C': 1, 'G': 2, 'U': 3, 'X': 4, '-': 5}
        num_bases = 6

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
            edges = self.pairing_rules(sequence=sequence, edges=edges, nodes_number=nodes_number)
            
        edges = list(set(edges))
        edge_index = torch.tensor(edges, dtype=torch.long).t().contiguous()
        
        graph_data = Data(x=node_features, edge_index=edge_index)

        if 'x_1' in data.columns:
            graph_data.y = torch.tensor(data[['x_1', 'y_1', 'z_1']].values, dtype=torch.float)

        graph_data.sequence = sequence
        graph_data.ID = data['ID'].iloc[0]
        return graph_data

    def process(self) -> None:

        for split in ['train', 'val', 'test']:

            df = self.preprocess(split)
            df = df.groupby(by=['ID'])
            
            pbar = tqdm(total=len(df))
            pbar.set_description(f'Processing {split} dataset ...')
            data_list = []

            for _, grouped in df:

                data = self.create_rna_graph(data=grouped)

                if self.pre_transform is not None:
                    data = self.pre_transform(data)
                
                data_list.append(data)
                pbar.update(1)
            pbar.close()
            self.save(data_list=data_list, path=osp.join(self.processed_dir, f'{split}.pt'))


