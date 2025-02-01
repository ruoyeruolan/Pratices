# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/01 15:16
@Description: 
"""

from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        for i in range(len(nums) - 1):

            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True
    
    def isArraySpecial_(self, nums: List[int]) -> bool:

        for i in range(len(nums) - 1):

            if (nums[i] & 1) ^ (nums[i + 1] & 1) == 0:
                return False
        return True