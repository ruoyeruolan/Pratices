# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/04 18:58
@Description: 
"""

from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        maxSum = 0
        lst = [nums[0]]

        for idx in range(1, n):

            if nums[idx] <= nums[idx - 1]:
                maxSum = max(maxSum, sum(lst))
                lst.clear()
            
            lst.append(nums[idx])
        return max(maxSum, sum(lst))
                


if __name__ == '__main__':
    # nums = [10,20,30,5,10,50]  # left = 3, right = 6
    nums = [12,17,15,13,10,11,12]
    s = Solution()
    s.maxAscendingSum(nums)