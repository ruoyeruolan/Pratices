# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/19 16:32
@Description: 
"""

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        total = 3 * 2 ** (n - 1)  # The first position has three choices, and the followings all have two choices, because s[i] != s[i - 1]
        
        if k > total:
            return ''
        
        res = ['a'] * n

        next_smallest = {'a': 'b', 'b': 'a', 'c': 'a'}
        next_greatest = {'a': 'c', 'b': 'c', 'c': 'b'}

        start_a = 1
        start_b = 2 ** (n - 1) + start_a
        start_c = 2 ** (n - 1) + start_b

        if k < start_b:
            res[0] = 'a'
            k -= 1

        elif k < start_c:
            res[0] = 'b'
            k -= 2 ** (n - 1) + 1

        else:
            res[0] = 'c'
            k -= start_c
        

        for idx in range(1, n):
            target = 2 ** (n - idx - 1)

            if k < target:
                res[idx] = next_smallest[res[idx - 1]]
            else:
                res[idx] = next_greatest[res[idx - 1]]
                k -= target
        return ''.join(res)
        
