# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/25 19:05
@Description: 
"""

from typing import List

from matplotlib.dates import MO
from polars import count

class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:

        MOD = 10**9 + 7

        n = len(arr)
        for idx in range(n):
            arr[idx] %= 2  # make elements be even or odd
        
        dpeven, dpodd = [0] * n, [0] * n
        if arr[n - 1] == 0:
            dpeven[n - 1] = 1
        else:
            dpodd[n - 1] = 1
        
        for idx in range(n - 2, -1, -1):
            if arr[idx] == 1:
                dpodd[idx] = (1 + dpeven[idx + 1]) % MOD
                dpeven[idx] = dpodd[idx + 1]
            
            else:
                dpeven[idx] = (1 + dpodd[idx + 1]) % MOD
                dpodd[idx] = dpeven[idx + 1]
        
        res = 0
        for odd in dpodd:
            res += odd
            res %= MOD
        return res
    
    def numOfSubarrays_(self, arr: List[int]) -> int:

        MOD = 10 ** 9 + 7
        res = prefixSum = 0

        odd_count, even_count = 0, 1

        for num in arr:

            prefixSum += num

            if prefixSum % 2 == 0:
                res += odd_count
                even_count += 1
            else:
                res += even_count
                odd_count += 1
        return res % MOD
                
