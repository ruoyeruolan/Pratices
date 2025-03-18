# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/18 04:55
@Description: 
"""

from collections import defaultdict

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:

        n = len(s)
        if n < k:
            return False
        
        charMap = defaultdict(int)
        for idx in range(n): charMap[s[idx]] += 1
        
        for idx in range(n - k + 1):
            curr = s[idx]
            
            if charMap[curr] < k:
                continue
            
            # temp = set(s[idx:idx+k])
            if all(s[idx + i] == curr for i in range(k)):
                prev = s[idx - 1] if idx > 0 else None
                after = s[idx + k] if idx + k < n else None

                if prev != curr and after != curr:
                    return True
        return False


if __name__ == '__main__':
    s = 'agichi'
    k = 2

    obj = Solution()
    obj.hasSpecialSubstring(s, k)