# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/27 17:46
@Description: 
"""

from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        n = len(arr)
        maxLength = 0

        dp = [[0] * n for _ in range(n)]

        for curr in range(2, n):

            start = 0
            prev = curr - 1

            while start < prev:
                target = arr[start] + arr[prev]

                if target > arr[curr]:
                    prev -= 1
                elif target < arr[curr]:
                    start += 1
                else:
                    dp[prev][curr] = dp[start][prev] + 1
                    maxLength = max(dp[prev][curr], maxLength)

                    prev -= 1
                    start += 1
        return maxLength + 2 if maxLength else 0


if __name__ == '__main__':

    arr = [1,3,7,11,12,14,18]
    s = Solution()
    s.lenLongestFibSubseq(arr)