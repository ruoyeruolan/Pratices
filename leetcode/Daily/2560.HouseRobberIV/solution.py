# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/15 18:22
# @Description: 

from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        min_, max_ = 1, max(nums)
        houses = len(nums)

        while min_ < max_:

            mid = (min_ + max_) // 2
            houses_stealed = 0

            idx = 0
            while idx < houses:
                if nums[idx] <= mid:
                    idx += 2
                    houses_stealed += 1
                else:
                    idx += 1

            if houses_stealed >= k:
                max_ = mid
            else:
                min_ = mid + 1
        return min_