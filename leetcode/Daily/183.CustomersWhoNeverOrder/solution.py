# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/13 22:07
@Description: 
"""

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        'Customers': customers.query('id not in @orders.customerId')['name'].tolist()
    })

if __name__ == '__main__':

    customers = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'name': ['John', 'Henry', 'Sam', 'Max']
    })

    orders = pd.DataFrame({
        'id': [1, 2],
        'customerId': [3, 1]
    })

    pd.DataFrame({
        'Customers': customers.query('id not in @orders.customerId')['name'].tolist()
    })
