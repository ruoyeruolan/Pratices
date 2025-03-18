# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/17 17:16
# @Description: 

from typing import List
from collections import defaultdict

class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        n = len(nums)
        freq = defaultdict(int)

        for idx in range(n):
            freq[nums[idx]] += 1
        
        for _, val in freq.items():

            if val % 2 != 0:
                return False
        return True