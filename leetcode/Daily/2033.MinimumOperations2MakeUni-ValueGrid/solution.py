# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/26 17:09
# @Description: 

from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        nrows, ncols = len(grid), len(grid[0])
        nums = []
        res = 0

        for row in range(nrows):
            for col in range(ncols):
                nums.append(grid[row][col])
        
        nums.sort()

        mid = nums[(nrows * ncols) // 2]
        for num in nums:
            if num % x != mid % x:
                return -1
            
            res += abs(mid - num) // x
        return res