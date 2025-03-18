# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/13 23:05
@Description: 
"""

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """Two Pointers"""
        
        nums.sort()
        n = len(nums)
        res = 10 ** 7

        for i in range(n - 2):
            left, right  = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                res = min(res, total, key=lambda x: abs(x - target))

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        return res
