# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/31 17:30
# @Description: 

from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        n = len(weights)
        pairWeights = [weights[i] + weights[i + 1] for i in range(n -1)]

        pairWeights.sort()

        res = 0
        for i in range(k - 1):
            res += pairWeights[n - 2 - 1] - pairWeights[i]
        return res