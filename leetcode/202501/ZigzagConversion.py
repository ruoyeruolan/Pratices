# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : ZigzagConversion.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/10 12:43
@Description: 
"""

def convert(s: str, numRows: int) -> str:

    if numRows == 1 or numRows >= len(s):
        return s
    
    zigzag = ['' for _ in range(numRows)]  # generate numRows number of strings
    row, step = 0, 1  # row is the current row, step is the direction of the row

    for i in s:

        zigzag[row] += i

        if row == 0:  
            step = 1
        
        elif row == numRows - 1:  # if the row is the last row, change the direction
            step = -1
        
        row += step  # move to the next row
    
    return ''.join(zigzag)