# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/13 18:53
@Description: 
"""

import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)

        numOperations = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            numOperations += 1
        return numOperations


if __name__ == '__main__':

    nums = [1,1,2,4,9]  # [2,11,10,1,3]
    k = 20

    s = Solution()
    s.minOperations(nums, k)
