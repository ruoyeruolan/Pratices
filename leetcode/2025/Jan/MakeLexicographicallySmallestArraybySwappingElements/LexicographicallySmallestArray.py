# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : LexicographicallySmallestArray.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/25 17:21
@Description: 
"""

from typing import List
from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        currGroup = 0
        num2Group = {}
        group2List = {}

        numSorted = sorted(nums)

        num2Group[numSorted[0]] = currGroup
        group2List[currGroup] = deque([numSorted[0]])

        for i in range(1,len(numSorted)):
            if abs(numSorted[i] - numSorted[i - 1]) > limit:
                currGroup += 1
            
            num2Group[numSorted[i]] = currGroup
            
            if currGroup not in group2List:
                group2List[currGroup] = deque()
            group2List[currGroup].append(numSorted[i])
        
        for i in range(len(nums)):
            num = nums[i]
            group = num2Group[num]
            nums[i] = group2List[group].popleft()
        return nums


if __name__ == '__main__':

    nums = [4,3,23,84,34,88,44,44,18,15]
    limit = 3

    solution = Solution()
    solution.lexicographicallySmallestArray(nums, limit)
