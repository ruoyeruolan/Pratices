# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/09 18:45
@Description: 
"""

from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        n = len(nums)
        goodPairs = 0
        hashMap = defaultdict(int)

        for i in range(n):
            diff = nums[i] - i

            if diff in hashMap:
                goodPairs += hashMap[diff]
            
            hashMap[diff] += 1
        
        totalPairs = n * (n - 1) // 2
        return totalPairs - goodPairs
        


if __name__ == '__main__':

    nums = [4,1,3,3]
    s = Solution()
    s.countBadPairs(nums)
