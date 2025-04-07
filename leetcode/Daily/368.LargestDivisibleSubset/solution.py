# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/04/06 18:23
# @Description: 

from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()

        dp = [1] * len(nums)
        prev = [-1] * len(nums)

        idx = 0
        for i in range(1, len(nums)):
            for j in range(i):

                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
            if dp[i] > dp[idx]:
                idx = i
        
        res = []
        while idx >= 0:
            res.append(nums[idx])
            if prev[idx] == -1:
                break
            idx = prev[idx]
        return res


