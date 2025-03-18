# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/16 20:04
@Description: Hash Table
"""

from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxLength = left = 0
        q = set()

        for idx in range(len(s)):

            while s[idx] in q:
                q.remove(s[left])
                left += 1
            
            q.add(s[idx])
            maxLength = max(maxLength, idx - left + 1)
        return maxLength
