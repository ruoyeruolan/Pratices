# -*- encoding: utf-8 -*-
"""
@Introduce  :
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/12 17:43
@Description:
"""
from collections import defaultdict
import heapq
from typing import List

from numpy import maximum_sctype
from sympy import li
from torch import ListType


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sumMap = defaultdict(list)
        for num in nums:
            digitSum = self.calculate_digit_sum(num)
            sumMap[digitSum].append(num)
        
        maxSum = -1
        for values in sumMap.values():
            if len(values) > 1:
                values.sort(reverse=True)
                maxSum = max(maxSum, values[0] + values[1])
        return maxSum
    
    def maximumSum_(self, nums: List[int]) -> int:
        sumMap = defaultdict(list)
        for num in nums:
            digitSum = self.calculate_digit_sum(num)
            heapq.heappush(sumMap[digitSum], num)

            if len(sumMap[digitSum]) > 2:
                heapq.heappop(sumMap[digitSum])
        
        maxSum = -1
        for values in sumMap.values():
            maxSum = max(maxSum, sum(values))
        return maxSum

    def calculate_digit_sum(self, num) -> int:
        digitSum = 0
        while num:
            num, digit = divmod(num, 10)
            digitSum += digit
        return digitSum


if __name__ == '__main__':

    num = 123
    s = Solution()
    s.calculate_digit_sum(num)