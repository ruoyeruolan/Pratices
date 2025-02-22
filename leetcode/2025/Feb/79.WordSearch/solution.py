# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/21 17:21
@Description: 
"""

from collections import defaultdict
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        nrow, ncol = len(board), len(board[0])
        visited = set()  # visited cells

        count = defaultdict(int)
        for char in word:
            count[char] += 1
        
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        
        for row in range(nrow):
            for col in range(ncol):
                if self.dfs(board, word, nrow, ncol, row, col, 0, visited):
                    return True

        return False
    
    def dfs(self, board, word, nrow, ncol, curr_row, curr_col, k, visited):
        
        if k == len(word): return True
        
        if (
            not self.isVaild(nrow, ncol, curr_row, curr_col) or 
            board[curr_row][curr_col] != word[k] or 
            (curr_row, curr_col) in visited
        ):
            return False
        
        visited.add((curr_row, curr_col))
        res = (
            self.dfs(board, word, nrow, ncol, curr_row + 1, curr_col, k + 1, visited) or 
            self.dfs(board, word, nrow, ncol, curr_row - 1, curr_col, k + 1, visited) or 
            self.dfs(board, word, nrow, ncol, curr_row, curr_col + 1, k + 1, visited) or 
            self.dfs(board, word, nrow, ncol, curr_row, curr_col - 1, k + 1, visited)
        )  # every time self.dfs run successfully, k + 1 to represent word paired one, if the k == len(word), all paired
        visited.remove((curr_row, curr_col))
        return res

    def isVaild(self, nrows, ncols, curr_row, curr_col) -> bool:
        return 0 <= curr_row < nrows and 0 <= curr_col < ncols


