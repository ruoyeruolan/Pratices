# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/03/03 17:52
@Description: 
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = 0, 0
        total = 0

        while left < right:

            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                total += left_max - height[left]
                left += 1

            else:
                total += right_max - height[right]
                right -= 1
        return total
