# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/04/08 16:47
# @Description: 

from typing import List
from collections import defaultdict

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        freq = defaultdict(int)

        for idx in range(n - 1, -1, -1):

            freq[nums[idx]] += 1

            if freq[nums[idx]] > 1:
                
                # if idx % 3 != 0:
                #     return idx // 3 + 1
                # return idx // 3
                return (idx + 1 + 2) // 3
        return 0
    
    def minimumOperations_(self, nums: List[int]) -> int:

        n = len(nums)
        seen = set()

        for idx in range(n - 1, -1, -1):

            if nums[idx] in seen:
                return (idx + 1 + 2) // 3
            
            seen.add(nums[idx])
        return 0


if __name__ == '__main__':

    nums = [4,5,6,4,4]
    s = Solution()
    s.minimumOperations(nums)