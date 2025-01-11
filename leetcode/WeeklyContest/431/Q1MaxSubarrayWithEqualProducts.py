# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : Q1MaxSubarrayWithEqualProducts.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/11 15:20
@Description: 
"""

# You are given an array of positive integers nums.

# An array `arr` is called product equivalent if `prod(arr) == lcm(arr) * gcd(arr)`, where:

# `prod(arr)` is the product of all elements of arr.
# `gcd(arr)` is the `GCD` of all elements of arr.
# `lcm(arr)` is the `LCM` of all elements of arr.
# Return the length of the longest product equivalent ***subarray*** of nums.


# Example 1:

# Input: nums = [1,2,1,2,1,1,1]

# Output: 5

# Explanation: 

# The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

# Example 2:

# Input: nums = [2,3,4,5,6]

# Output: 3

# Explanation: 

# The longest product equivalent subarray is [3, 4, 5].

# Example 3:

# Input: nums = [1,2,3,1,4,5,1]

# Output: 5

# Note: Please do not copy the description during the contest to maintain the integrity of your submissions.©leetcode

from typing import List

import numpy as np

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        
        res, left = 1, 0

        while left < len(nums):
            right = left
            while right < len(nums):
                if np.prod(nums[left:right+1]) == np.lcm.reduce(nums[left:right+1])*np.gcd.reduce(nums[left:right+1]):
                    res = max(res, right-left+1)
                right += 1
            left += 1
        return res


if __name__ == '__main__':

    nums = [1,2,1,2,1,1,1]
    nums = [2,3,4,5,6]

    s = Solution()
    s.maxLength(nums=nums)