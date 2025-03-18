# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/16 19:49
@Description: Hash Table
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}
        for idx in range(len(nums)):
            diff = target - nums[idx]

            if diff in hashMap:
                return [idx, hashMap[diff]]
            hashMap[diff] = idx
        return []

            