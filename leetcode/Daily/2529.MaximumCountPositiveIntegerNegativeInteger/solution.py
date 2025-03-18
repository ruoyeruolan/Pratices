# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/12 18:20
# @Description: 

from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        n = len(nums)
        pos = neg = idx = 0

        while idx < n:

            if nums[idx] < 0:
                neg += 1
            elif nums[idx] > 0:
                pos += 1
            idx += 1
        return max(pos, neg)
   
    def lower_bound(self, nums):
        start, end = 0, len(nums) - 1
        index = len(nums)

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] < 0:
                start = mid + 1
            else:
                end = mid - 1
                index = mid

        return index

    # Return the first index where the value is greater than zero.
    def upper_bound(self, nums):
        start, end = 0, len(nums) - 1
        index = len(nums)

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] <= 0:
                start = mid + 1
            else:
                end = mid - 1
                index = mid

        return index

    def maximumCount_(self, nums):
        # All integers from the first non-zero to last will be positive
        # integers.
        positiveCount = len(nums) - self.upper_bound(nums)
        # All integers from the index 0 to index before the first zero index
        # will be negative.
        negativeCount = self.lower_bound(nums)

        return max(positiveCount, negativeCount) 