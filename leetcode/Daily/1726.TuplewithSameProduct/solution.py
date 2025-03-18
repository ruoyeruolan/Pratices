# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/06 18:34
@Description: 
"""

from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        numsLength = len(nums)
        pairProductsFrequency = {}
        totalNumberoftuples = 0

        for firstindex in range(numsLength):
            for secondIndex in range(firstindex + 1, numsLength):
                value = nums[firstindex] * nums[secondIndex]
                if value in pairProductsFrequency:
                    pairProductsFrequency[value] += 1
                else:
                    pairProductsFrequency[value] = 1
        
        for _, val in pairProductsFrequency.items():
            pairsOfEqualProduct = (val - 1) * val // 2
            totalNumberoftuples += 8 * pairsOfEqualProduct
        return totalNumberoftuples
        