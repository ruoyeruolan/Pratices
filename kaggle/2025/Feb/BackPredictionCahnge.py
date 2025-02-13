# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : BackPredictionCahnge.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/11 18:47
@Description: 
"""

import optuna
import pandas as pd
from category_encoders import TargetEncoder
from sklearn.metrics import mean_squared_error, root_mean_squared_error
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from xgboost import XGBRegressor

def objective_xg(trial, X_train, X_test, y_train, y_test):

    params = {
        "n_estimators": 70,
        "eval_metric": "rmse",
        "max_depth": trial.suggest_int("max_depth", 3, 7),
        "learning_rate": trial.suggest_loguniform("learning_rate", 0.01, 0.1),
        "min_child_weight": trial.suggest_int("min_child_weight", 0.01, 1),
        "subsample": trial.suggest_loguniform("subsample", 0.1, 1.0),
        "colsample_bylevel": trial.suggest_float("colsample_bylevel", 0.1, 1),
        "colsample_bytree": trial.suggest_float("colsample_bytree", 0.1, 1),
        "colsample_bynode": trial.suggest_float("colsample_bynode", 0.1, 1),
        "reg_alpha": trial.suggest_float("reg_alpha", 0.01, 1),
        "reg_lambda": trial.suggest_float("reg_lambda", 0.01, 1)
    }

    model =  XGBRegressor(**params, enable_categorical = True)
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    return root_mean_squared_error(y_test, y_pred, squared = False)


def main():

    data = pd.read_csv('/kaggle/input/playground-series-s5e2/train.csv', index_col=0)
    target = data['Price']
    
    test = pd.read_csv('/kaggle/input/playground-series-s5e2/test.csv', index_col=0)

    encoder = TargetEncoder(verbose=1, drop_invariant=True, return_df=True, min_samples_leaf=20, smoothing=10)
    encoder = encoder.fit(data.drop(columns='Price'), target)
    data = encoder.transform(data.drop(columns='Price'))
    test = encoder.transform(test)

    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)
    trial = optuna.create_study(direction="minimize")
    optuna.logging.set_verbosity(optuna.logging.WARNING)
    trial.optimize(
        objective_xg(X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test), n_trials=5, show_progress_bar=True)