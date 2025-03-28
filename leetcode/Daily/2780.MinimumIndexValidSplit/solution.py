# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/27 18:04
# @Description: 

from typing import List
from collections import defaultdict

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        firstMap = defaultdict(int)
        secondMap = defaultdict(int)

        for num in nums:
            secondMap[num] += 1
        
        for idx in range(n):
            
            num = nums[idx]
            firstMap[num] += 1
            secondMap[num] -= 1

            if (
                firstMap[num] * 2 > idx + 1 and
                secondMap[num] * 2 > n - idx - 1
            ):
                return idx
        return -1
    
    def minimumIndex_(self, nums: List[int]) -> int:

        n = len(nums)
        x = nums[0]
        count = x_count = 0

        for num in nums:

            if num == x:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                x = num
                count = 1
        
        for num in nums:
            if num == x:
                x_count += 1

        count = 0
        for idx in range(n):
            if nums[idx] == x:
                count += 1
            
            remain = x_count - count
            if count * 2 > idx + 1 and remain * 2 > n - idx - 1:
                return idx
        return -1