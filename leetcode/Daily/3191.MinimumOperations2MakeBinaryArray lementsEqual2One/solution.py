# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/19 17:09
# @Description: 

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = 0

        for idx in range(n - 2):
            if nums[idx] == 0:
                nums[idx] = 1
                nums[idx + 1] ^= 1
                nums[idx + 2] ^= 1

                count += 1
        
        if nums[n - 2] == 0 or nums[n - 1] == 0:  # sum(nums) == n:
            return -1
        return count
    
    def minOperations_sliding_window(self, nums: List[int]) -> int:

        n = len(nums)
        count = 0

        for idx in range(2, n):
            
            if nums[idx - 2] == 0:
                nums[idx] ^= 1
                nums[idx - 1] ^= 1
                nums[idx - 2] ^= 1

                count += 1
        
        if sum(nums) == n:
            return count
        return -1
