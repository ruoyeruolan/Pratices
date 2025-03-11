# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/11 17:29
# @Description: 

from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        freq = defaultdict(int)
        count = start = end = 0
        n = len(s)

        while end < n:
            freq[s[end]] += 1

            while len(freq) == 3:

                count += n - end
                freq[s[start]] -= 1

                if freq[s[start]] == 0: freq.pop(s[start])
                
                start += 1
            end +=1
        return count
    
    def numberOfSubstrings_(self, s: str) -> int:

        count = 0
        last_position = [-1] * 3

        for pos in range(len(s)):
            
            last_position[ord(s[pos]) - ord('a')] = pos

            count += 1 + min(last_position)
        return count