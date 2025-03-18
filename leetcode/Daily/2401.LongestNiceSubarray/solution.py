# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/18 18:50
# @Description: 

from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        n, used, start, length = len(nums), 0, 0, 0

        for end in range(n):

            while used & nums[end] != 0:

                used ^= nums[start]
                start += 1
            
            used |= nums[end]

            length = max(length, end - start + 1)
        return length
    
    
