# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/03/03 15:29
@Description: 
"""

from typing import List

from matplotlib.colors import same_color

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        n = len(nums)
        smaller = []
        greater = []
        equal = []

        for idx in range(n):

            if nums[idx] < pivot:
                smaller.append(nums[idx])
            elif nums[idx] > pivot:
                greater.append(nums[idx])
            else:
                equal.append(nums[idx])
        return smaller + equal + greater

    def pivotArray_(self, nums: List[int], pivot: int) -> List[int]:

        n = len(nums)
        smaller, greater = 0, n - 1
        res = [0] * n

        for i, j in zip(range(n), range(n, -1, -1)):

            if nums[i] < pivot:
                res[smaller] = nums[i]
                smaller += 1
            
            if nums[greater] > pivot:
                res[j] = nums[j]
                j -= 1
        
        while smaller <= greater:
            res[smaller] = pivot
            smaller += 1
        return res