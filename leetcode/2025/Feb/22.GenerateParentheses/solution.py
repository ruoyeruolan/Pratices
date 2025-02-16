# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/16 06:37
@Description: 
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(res, '', 0, 0, n)
        return res
    
    def backtrack(self, res: List[str], cur: str, open: int, close: int, max: int):
        if len(cur) == max * 2:
            res.append(cur)
        
        if open < max:
            self.backtrack(res, cur + '(', open + 1, close, max)
        
        if close < open:
            self.backtrack(res, cur + ')', open, close + 1, max)
