# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/14 18:06
@Description: 
"""

from typing import List

from sklearn.utils import resample
from torch import K


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        return self.kSum(nums, target, 4)

    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        res = []

        if not nums: return res

        average_value = target // k
        if average_value < nums[0] or average_value > nums[-1]:
            return res
        
        if k == 2:
            return self.twoSum(nums, target)
        
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for subset in self.kSum(nums[i + 1:], target - nums[i], k - 1):
                    res.append([nums[i]] + subset)
        return res
    
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        lo, hi = 0, n - 1

        while lo < hi:
            cSum = nums[lo] + nums[hi]
            if cSum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif cSum > target or (hi < n - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
        return res
    
    def twoSum_(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        s = set()

        for i in range(len(nums)):
            if len(res) == 0 or res[-1][1] != nums[i]:
                complement = target - nums[i]

                if complement in s:
                    res.append([complement, nums[i]])
            s.add(nums[i])
        return res
