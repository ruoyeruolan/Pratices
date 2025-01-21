# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : DuplicateEmails.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/21 21:07
@Description: 
"""

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # person.groupby(by=['email']).filter(lambda x: len(x) > 1).drop_duplicates(subset=['email']).iloc[:, 1:]

    return person.groupby('email').nunique().query('id > 1').index.to_frame().reset_index(drop=True)
   


if __name__ == '__main__':
    
    person = pd.DataFrame({
        'id': [1, 2, 3],
        'email': ['a@b.com', 'c@d.com', 'a@b.com']
    })
    

    