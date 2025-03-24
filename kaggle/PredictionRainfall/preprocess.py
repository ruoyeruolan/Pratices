# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : preprocess.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/19 20:01
# @Description: Version 1: 0.86645 

from typing import Tuple, Optional

import optuna
import numpy as np
import pandas as pd
import xgboost as xgb

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def data_process(fname: str = 'train') -> Tuple[np.ndarray, Optional[np.ndarray]]:
    df = pd.read_csv(f'./data/PredictionRainfall/{fname}.csv', index_col=0)
    
    
    y = None
    if 'rainfall' in df.columns:
        X = StandardScaler().fit_transform(df.drop(columns=['rainfall']))
        y = df['rainfall'].to_numpy()

    return X, y

def objective(trial:optuna.trial.Trial):

    X, y = data_process()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)
    params = {
        'n_estimators': trial.suggest_int(name='n_estimators', low=50, high=100),
        'max_depth': trial.suggest_int(name='max_depth', low=2, high=10),
        'max_leaves': trial.suggest_int(name='max_leaves', low=3, high=20),
        'grow_policy': trial.suggest_categorical(name='grow_policy', choices=['depthwise', 'lossguide']),
        'learning_rate': trial.suggest_float(name='learning_rate', low=.001, high=.1),
        'subsample': trial.suggest_float(name='subsample', low=.1, high=1),
        'reg_alpha': trial.suggest_float(name='reg_alpha', low=.01, high=1),
        'reg_lambda': trial.suggest_float(name='reg_lambda', low=.01, high=1.0),
    }

    cls = xgb.XGBRegressor(**params)
    cls.fit(X_train, y_train)
    y_pred = cls.predict(X_test)
    return float(mean_squared_error(y_test, y_pred))

def get_best_params():
    study = optuna.create_study(direction='minimize')
    study.optimize(objective, n_trials=20, show_progress_bar=True)
    return study.best_params

def main():

    X, y = data_process()
    params = get_best_params()

    cls = xgb.XGBRegressor(**params)
    cls.fit(X, y)

    data = data_process('test')
    cls.predict(data)
