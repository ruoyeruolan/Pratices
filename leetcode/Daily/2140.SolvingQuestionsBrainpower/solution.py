# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/04/01 19:03
# @Description: 

from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        dp = [0] * n

        for idx in range(n - 1, -1, -1):

            index = idx + questions[idx][1] + 1

            if index < n:
                dp[idx] = dp[index] + questions[idx][0]
            else:
                dp[idx] = questions[idx][0]
            
            if idx < n - 1:
                dp[idx] = max(dp[idx], dp[idx + 1])
        return dp[0]
    
    def mostPoint_(self, questions: List[List[int]]) -> int:

        dp = [0] * len(questions)

        def backtrace(idx: int) -> int:

            if idx >= len(questions):
                return 0
            
            if dp[idx]:
                return dp[idx]
            
            points, brainpower = questions[idx]
            dp[idx] =  max(
                backtrace(idx + 1),
                points + backtrace(idx + 1 + brainpower)
            )
            return dp[idx]
        return backtrace(0)