# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/04/07 17:56
# @Description: 

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        target = total // 2

        if total % 2 != 0:
            return False
        
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for idx in range(target, num - 1, -1):
                dp[idx] = dp[idx] or dp[idx - num]
        return dp[target]


if __name__ == '__main__':

    nums = [1,5,11,5]

    s = Solution()
    s.canPartition(nums)


