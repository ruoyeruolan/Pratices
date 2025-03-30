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

import numpy as np
import pandas as pd

import torch
import torch.nn as nn
import torch.nn.functional as F

from torch import Tensor
from torch_geometric.io import fs
from torch_geometric.data import Data, InMemoryDataset
from torch_geometric.data import extract_zip


class RNA3DFolding(InMemoryDataset):

    url = 'https://www.kaggle.com/competitions/87793/download-all'

    def __init__(
            self, 
            root: str | None = None, 
            split: str | None = 'train',
            transform: Callable[..., Any] | None = None, 
            pre_transform: Callable[..., Any] | None = None, 
            pre_filter: Callable[..., Any] | None = None, 
            # log: bool = True, 
            force_reload: bool = False
    ) -> None:
        assert split in ['train', 'test', 'validation']
        super().__init__(
            root, transform, pre_transform,
            pre_filter, force_reload=force_reload
        )

        # if not callable(self.log):
        #     self.log = lambda x: None

        # self.raw_dir = self.raw_dir
        path = osp.join(self.processed_dir, f'{split}.pt')
        self.load(path=path)

    
    @property
    def raw_file_names(self) -> List[str]:
        return [
            'test_sequences.csv',
            'train_sequences.csv', 'train_labels.csv',
            'validation_sequences.csv', 'validation_labels.csv'
        ]
    
    @property
    def processed_dir(self) -> str:
        return osp.join(self.root, 'full', 'processed')
    
    @property
    def processed_file_names(self) -> List[str]:
        return ['train.pt', 'test.pt', 'validation.pt']
    
    def download(self) -> None:
        fs.rm(self.raw_dir)
        # if not osp.exists(osp.join(self.root, 'stanford-rna-3d-folding.zip')):
        path = f'{self.root}/stanford-rna-3d-folding.zip'

        if not osp.exists(f'{self.root}/stanford-rna-3d-folding'):
            extract_zip(path=path, folder=f'{self.root}/stanford-rna-3d-folding')
        os.rename(osp.join(self.root, 'stanford-rna-3d-folding'), self.raw_dir)
    
    def preprocess(self, fname: str = 'train') -> dict:

        dit = {'A': 0, 'C': 1, 'G': 2, 'U': 3, 'X': 4, '-': 5}
        data = pd.read_csv(osp.join(self.raw_dir, f'{fname}_sequences.csv'))

        if fname == 'train':
            data['temporal_cutoff'] = data['temporal_cutoff'].apply(pd.to_datetime)
            cut_off = pd.Timestamp('2022-05-27')
            data = data.query(f'temporal_cutoff < "{cut_off}"')

        print('Encoding Sequence ...')
        nrows, _ = data.shape
        data = data.assign(seq=[
            torch.tensor([dit[base] for base in seq], dtype=torch.float64)
            for seq in tqdm(data['sequence'], total=nrows)
        ])

        if fname != 'test':
            labels = pd.read_csv(osp.join(self.raw_dir, f'{fname}_labels.csv'))
            labels = labels.assign(ID=labels['ID'].str.replace(r'_\d+$', '', regex=True))

            grouped = labels.groupby('ID')
            
            print('Processing labels ...')
            data = data.assign(labels=[
                torch.tensor(grouped.get_group(group)[['x_1', 'y_1', 'z_1']].values) 
                for group in tqdm(data['target_id'], total=nrows)
            ])
        
        print('Creating adjacency Matrix ...')
        data = data.assign(
            adj=[self.create_rna_adjacency_matrix(seq) for seq in tqdm(data['sequence'], total=nrows)]
        )
        return data.to_dict(orient='index')
    
    def create_rna_adjacency_matrix(self, sequence: str) -> Tensor:
        n = len(sequence)
        
        seq_array = np.fromiter(sequence, dtype='U1', count=n)

        adj = np.zeros((n ,n), dtype=np.int8)
        pairs_types = {
            ('A', 'U'): 1,
            ('G', 'C'): 2,
            ('G', 'U'): 3,
            
            ('A', 'G'): 4,
            ('C', 'U'): 5,
            ('A', 'C'): 6,
            ('U', 'U'): 7,
            ('G', 'G'): 8,
            ('C', 'C'): 9,
            ('A', 'A'): 10,
        }

        for (base1, base2), bond_type in pairs_types.items():
            mask = (seq_array == base1)[:, None] & (seq_array == base2)[None, :]
            adj[mask] = bond_type
            adj[mask.T] = bond_type

        np.fill_diagonal(adj, 0)
        return torch.tensor(adj, dtype=torch.long) 
    
    def process(self) -> None:
        
        for split in ['train', 'validation', 'test']:
            dit = self.preprocess(split)
            
            n = len(dit)

            pbar = tqdm(total=n)
            pbar.set_description(f'Processing {split} dataset ...')

            data_list =[]
            for key in dit.keys():
                mols = dit[key]

                x: Tensor = mols['seq'].to(torch.long).view(-1, 1)
                y: Tensor | None = mols['labels'].to(torch.float) if 'labels' in mols else None

                adj: Tensor = mols['adj']
                edge_index = adj.nonzero(as_tuple=False).t().contiguous()
                edge_attr = adj[edge_index[0], edge_index[1]].to(torch.long)

                data = Data(x=x, edge_index=edge_index, edge_attr=edge_attr, y=y)

                if self.pre_filter is not None and self.pre_filter(data):
                    continue

                if self.pre_transform is not None:
                    data = self.pre_transform(data)
                
                data_list.append(data)
                pbar.update(1)
            pbar.close()
            self.save(data_list=data_list, path=osp.join(self.processed_dir, f'{split}.pt'))


if __name__ == '__main__':

    root = '/public/workspace/ryrl/IdeaProjects/Projects/torch/pyGenometrics/Cases/rna3d/'
    train = RNA3DFolding(root=root, split='train')
    print(train)
