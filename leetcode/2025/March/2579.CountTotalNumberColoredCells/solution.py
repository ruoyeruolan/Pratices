# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/05 17:24
# @Description: 

class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n ** 2 - 2 * n + 1