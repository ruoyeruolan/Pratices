# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : ReverseInteger.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/10 14:21
@Description: 
"""

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21

def reverse(x: int) -> int:
    
    # if x == 0: 
    #     return 0
    
    if x < 0:
        x = -int(str(x)[::-1][:-1])
    else:
        x = int(str(x)[::-1])
    
    if x < -2**31 or x > 2**31 - 1:
        return 0
    return x


def reverse_(x: int) -> int:
    
    res, sign = 0, 1 if x > 0 else -1
    
    x = abs(x)

    while x != 0:
        res = res * 10 + x % 10
        x = x // 10
    
    if res < -2**31 or res > 2**31 - 1:
        return 0
    return res * sign