# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : MinimizeXOR.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/15 18:14
@Description: 
"""
# Given two positive integers num1 and num2, find the positive integer x such that:
# `x` has the same number of set bits as `num2`, and
# The value `x XOR num1` is minimal.
# Note that `XOR` is the bitwise `XOR` operation.

# Return the integer `x`. The test cases are generated such that `x` is uniquely determined.
# The number of **set bits** of an integer is the number of `1`'s in its binary representation.

# Example 1:
# Input: num1 = 3, num2 = 5
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0011 and 0101, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
# Example 2:

# Input: num1 = 1, num2 = 12
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0001 and 1100, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count_num1 = bin(num1).count('1')
        count_num2 = bin(num2).count('1')

        for i in range(32):
            if count_num1 == count_num2:
                break
            
            if count_num1 > count_num2:
                if num1 & (1 << i):
                    num1 &= ~(1 << i)
                    count_num1 -= 1
            else:
                if not (num1 & (1 << i)):
                    num1 |= (1 << i)  # num1[i] = 1 
                    count_num1 += 1
        return num1



if __name__ == '__main__':
    num1 = 7
    num2 = 12

    s = Solution()
    s.minimizeXor(num1, num2)
    
    bin(num1).count('1')
    bin(num2).count('1')
    bin(12)

    count_num1 = bin(num1).count('1')
    count_num2 = bin(num2).count('1') 
    total_bits = len(bin(num1)) - 2
    mask = ~(1 << total_bits - count_num2 - 1)
    num1 & mask