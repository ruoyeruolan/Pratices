# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/03/03 17:44
@Description: 
"""

class Solution:
    def isHappy(self, n: int) -> bool:

        while n != 1 and n != 4:
            Sum = 0
            while n > 0:
                Sum += (n % 10) ** 2
                n //= 10
            n = Sum
        return n == 1