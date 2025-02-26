# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/26 18:24
@Description: 
"""

from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        n = len(nums)

        prefixSum = minimum = maximum = 0

        for idx in range(n):

            prefixSum += nums[idx]

            minimum = min(minimum, prefixSum)
            maximum = max(maximum, prefixSum)
        return maximum - minimum