# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : soluyion.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/03 16:02
@Description: 
"""

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incrLen = descLen = maxLen = 1

        for idx in range(len(nums) - 1):

            if nums[idx + 1] > nums[idx]:
                incrLen += 1
                descLen = 1  # If the first two element is increased, you should reset descLen otherwise the first desc's length will 2. If the following desc is continues it will never enter this branch, otherwise the length of desc should be reset again.

            elif nums[idx + 1] < nums[idx]:
                descLen += 1
                incrLen = 1

            else:
                incrLen = descLen = 1  # if elements are equal, the length of both incr and desc should be reset. Count Break! 
        
        return max(maxLen, incrLen, descLen)


if __name__ == '__main__':
    nums = [3,3,3,3]
    s = Solution()
    s.longestMonotonicSubarray(nums)