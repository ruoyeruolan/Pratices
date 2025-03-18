# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/03/03 17:04
@Description: 
"""

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        left = n - 2

        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1
        
        if left >= 0:
            
            right = n - 1
            while right >= 0 and nums[right] <= nums[left]:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        
        left, right = left + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        