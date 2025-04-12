# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/04/11 17:29
# @Description: 

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        res = 0
        for i in range(low, high + 1):

            if i < 100 and i % 11 == 0:
                res += 1
            
            if 1000 <= i <= 10000:
                left = i // 1000 + i % 1000 // 100
                right = i % 100 // 10 + i % 10

                if left == right:
                    res += 1
        return res