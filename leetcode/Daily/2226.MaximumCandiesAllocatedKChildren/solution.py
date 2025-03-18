# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/14 18:13
# @Description: 

from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        candies.sort()

        left, right = 0, candies[-1]

        while left < right:

            mid = (left + right + 1) // 2

            if self.can_allocate_candies(candies, k, mid):
                left = mid
            else:
                right = mid - 1
        return left
    
    def can_allocate_candies(self, candies, k, num_candies):

        max_num_of_children = 0

        for pile in candies:
            max_num_of_children += pile // num_candies
        return max_num_of_children >= k



        