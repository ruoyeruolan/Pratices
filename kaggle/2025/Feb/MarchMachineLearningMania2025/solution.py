# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/18 22:38
@Description: 
"""

import os
import pandas as pd

os.getcwd()

df = pd.read_csv('./2025/Feb/MarchMachineLearningMania2025/data/MTeams.csv')
df_ = pd.read_csv('./2025/Feb/MarchMachineLearningMania2025/data/WTeams.csv')

df.head()
df_.head()

df.melt(id_vars=['A'], value_vars=['B'], var_name=)