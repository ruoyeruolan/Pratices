# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : preprocess.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/10 22:23
# @Description: 

import pandas as pd


def preprocess():
    train = pd.read_csv('/Users/wakala/IdeaProjects/Practices/kaggle/train_sequences.csv')
    dit = train.set_index('target_id').to_dict()
    labels = pd.read_csv('/kaggle/input/stanford-rna-3d-folding/train_labels.csv')
    labels['ID'] = labels['ID'].str.replace('_\d+$', '', regex=True)
    labels = labels.assign(**{key: labels['ID'].map(val) for key, val in dit.items()})
    labels = pd.concat([labels.iloc[:, 0], labels.iloc[:, 6], labels.iloc[:, 1:6], labels.iloc[:, 7:]], axis=1)
    labels['temporal_cutoff'] = labels['temporal_cutoff'].apply(pd.to_datetime)
    # labels.head()
    return labels