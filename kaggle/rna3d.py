# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : rna3d.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/19 19:21
# @Description: 

import polars as pl
import torch.nn as nn
from torch import Tensor

seq = pl.read_csv('/Users/wakala/IdeaProjects/Practices/kaggle/data/RNA3D/train_sequences.csv')
label = pl.read_csv('/Users/wakala/IdeaProjects/Practices/kaggle/data/RNA3D/train_labels.csv')

seq.select(["target_id", pl.all().exclude("target_id")]).to_dict(as_series=False) 
seq['target_id'].is_duplicated().sum()