# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution_.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/04/03 17:44
# @Description: 

from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        res, diffMax, valMax = 0, 0, 0

        for k in range(len(nums)):

            res = max(res, diffMax * nums[k])
            diffMax = max(diffMax, valMax - nums[k])
            valMax = max(valMax, nums[k])
        return res