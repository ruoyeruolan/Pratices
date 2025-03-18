# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/11 15:07
@Description: 
"""

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        n = len(part)        
        while part in s:

            start = s.find(part)

            s = s[:start] + s[start + n:]
        return s



if __name__ == '__main__':

    s = "axxxxyyyyb"
    part = "xy"

    s.find(part)
