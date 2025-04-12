# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/04/09 17:55
# @Description: 

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        seen = set()

        for num in nums:
            if num < k:
                return -1
            elif num > k:
                seen.add(num)
        return len(seen)