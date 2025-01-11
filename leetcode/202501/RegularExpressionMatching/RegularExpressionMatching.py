# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       :  regular_expression_matching.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/11 16:24
@Description: 

        Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        The matching should cover the entire input string (not partial).
"""

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" doesn't match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

import re

class Solution:

    @staticmethod
    def isMatch(s: str, p: str) -> bool:
        return bool(re.fullmatch(p, s))
    
    def isMatch_(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':  # if `*` in p,
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])
    
    def isMatchDp(self, s: str, p: str):  # dynamic programming
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                first_match = i < m and (s[i] == p[j] or p[j] == '.')
                if j + 1 < n and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0], dp


if __name__ == '__main__':

    s = "aaaabbab"
    p = "a*"

    solution = Solution()
    solution.isMatch(p, s)
    solution.isMatch_(p, s)
    b, dp = solution.isMatchDp(p, s)
    len(s)