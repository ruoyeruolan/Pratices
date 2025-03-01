# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/03/01 16:34
@Description: 
"""

from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = []

        for idx in range(n - 1):

            if nums[idx] == nums[idx + 1] and nums[idx] != 0:
                nums[idx] *= 2
                nums[idx + 1] = 0
        
        for idx in range(n):
            if nums[idx] != 0:
                res.append(nums[idx])
        
        for _ in range(n - len(res)):

            res.append(0)
        return res