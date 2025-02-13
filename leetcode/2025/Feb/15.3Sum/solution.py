# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/10 21:05
@Description: 
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Two Pointers"""
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            k = n - 1
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                while j < k and nums[j] + nums[k] > target:
                    k -= 1
                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
        return res
    
    def threeSum_(self, nums: List[int]) -> List[List[int]]:
        """Hash Table"""

        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # skip the same number
                continue

            target = -nums[i]
            hashtable = set()
            for j in range(i + 1, n):
                complement = target - nums[j]

                if complement in hashtable:
                    res.add((nums[i], nums[j], complement))
                hashtable.add(nums[j])
        return [list(triplet) for triplet in res]
