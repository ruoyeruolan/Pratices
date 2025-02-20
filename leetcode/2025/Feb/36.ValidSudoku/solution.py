# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/20 19:47
@Description: HashTable 
"""

from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        box_dict = defaultdict(set)

        for row in range(9):
            for col in range(9):

                if board[row][col] == '.':
                    continue
                
                temp = board[row][col]
                if  temp in row_dict[row] or temp in col_dict[col] or temp in box_dict[(row // 3, col // 3)]:
                    return False
                
                row_dict[row].add(board[row][col])
                col_dict[col].add(board[row][col])
                box_dict[(row // 3, col // 3)].add(board[row][col])
        return True
