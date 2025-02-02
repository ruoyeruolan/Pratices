# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/02 15:47
@Description: 
"""

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n <= 1:
            return True
        
        counts = 0
        for idx in range(1, n):
            if nums[idx] < nums[idx - 1]:
                counts += 1
            
        if nums[0] < nums[n -1]:
            counts += 1
        return counts <= 1