# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/05 16:26
@Description: 
"""

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        # if set(s1) != set(s2):
        #     return False

        # if s1 == s2:
        #     return True

        n = len(s1)
        misMatch = 0
        misMatchIndex1 = 0
        misMatchIndex2 = 0
        for idx in range(n):
            if s1[idx] != s2[idx]:
                misMatch += 1

                if misMatch > 2:
                    return False
                
                elif misMatch == 1:
                    misMatchIndex1 = idx
                else:
                    misMatchIndex2 = idx
        return s1[misMatchIndex1] == s2[misMatchIndex2] and s1[misMatchIndex2] == s2[misMatchIndex1]


                           

if __name__ == '__main__':
    # s1 = "bank"
    # s2 = "kanb"
    # s1 = "attack"
    # s2 = "defend"
    # # s1 = "kelb"
    # s2 = "kelb"
    s1 = 'caa'
    s2 = 'aaz'

    s = Solution()
    s.areAlmostEqual(s1, s2)