# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : LongestPalindromicSubstring.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/10 00:03
@Description: 
"""
import pandas as pd
s = 'babad'
s[3]
def longestPalindrome(s: str) -> str:
    l = 0
    res = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                
                a = j - i + 1

                if a >= l:
                    l = a
                    res = s[i:j+1]
                
    return res


def longestPallindrome(s: str) -> str:

    if len(s) < 2 or s == s[::-1]:
        return s
    
    def expand_(s : str, left: int, right: int):  # find the pallindrome substring
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    res = ''
    for i in range(len(s)):
        res = max(expand_(s, i, i), expand_(s, i, i+1), res, key=len)  # compare the length of the pallindrome substring
    return res

    