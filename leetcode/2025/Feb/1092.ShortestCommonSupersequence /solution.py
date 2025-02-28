# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/28 16:58
@Description: 
"""

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        n1, n2 = len(str1), len(str2)

        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for row in range(n1 + 1):
            dp[row][0] = row
        
        for col in range(n2 + 1):
            dp[0][col] = col
        
        for row in range(1, n1 + 1):
            for col in range(1, n2 + 1):
                if str1[row - 1] == str2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = min(dp[row][col - 1], dp[row - 1][col]) + 1
        
        sequence = []
        row, col = n1, n2
        while row > 0 and col > 0:

            if str1[row - 1] == str2[col - 1]:
                sequence.append(str1[row - 1])
                row -= 1
                col -= 1
            elif dp[row - 1][col] < dp[row][col - 1]:
                sequence.append(str1[row - 1])
                row -= 1
            else:
                sequence.append(str2[col - 1])
                col -= 1
        
        while row > 0:
            sequence.append(str1[row - 1])
            row -= 1
        
        while col > 0:
            sequence.append(str2[col - 1])
            col -= 1
        return ''.join(sequence[::-1])