# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/04/02 17:08
# @Description: 

from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        n = len(nums)
        res, diffMax, valMax = 0, 0, 0

        for idx in range(n):

            res = max(res, diffMax * nums[idx])
            diffMax = max(diffMax, valMax - nums[idx])
            valMax = max(valMax, nums[idx])
        return res



