# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/14 18:56
@Description: 
"""
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    
    df = employee.merge(
        department, how='left', left_on='departmentId', right_on='id'
    )

    df = df[df['salary'] == df.groupby(by=['name_y'])['salary'].transform('max')][['name_y', 'name_x', 'salary']]
    df.columns = ['Department', 'Employee', 'Salary']
    return df



if __name__ == "__main__":
    
    employee = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "name": ["Joe", "Jim", "Henry", "Sam", "Max"],
        "salary": [70000, 90000, 80000, 60000, 900000],
        "departmentId": [1, 1, 2, 2, 1]
    })
    
    department = pd.DataFrame({
        "id": [1, 2],
        "name": ["IT", "Sales"]
    })

    df = employee.merge(
        department, how='left', left_on='departmentId', right_on='id'
    )  # .groupby(by=['name_B'])['salary'].idxmax()

    df[df['salary'] == df.groupby(by=['name_y'])['salary'].transform('max')]
    
    
    df.columns = ['Department', 'Employee', 'Salary']

    department_highest_salary(employee, department)
    