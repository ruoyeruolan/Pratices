# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/07 18:51
# @Description: 


from typing import List

from numpy import diff

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        sieve = self.sieveArray(right)
        isPrimes = [num for num in range(left, right + 1) if sieve[num]]

        if len(isPrimes) < 2:
            return [-1, -1]
        
        ans = [-1, -1]
        minimum = float('inf')
        for idx in range(1, len(isPrimes)):
            difference = isPrimes[idx] - isPrimes[idx - 1]
            if difference < minimum:
                minimum = difference
                ans = [isPrimes[idx - 1], isPrimes[idx]]
        return ans

    def sieveArray(self, right: int):

        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 is not prime

        for num in range(2, int(right ** .5) + 1):
            if sieve[num]:
                for mp in range(num * num, right + 1, num):
                    sieve[mp] = False
        return sieve
    
    def isPrimes(self, num):

        if num < 2:
            return False
        
        if num == 2 or num == 3:
            return True
        
        if num % 2 == 0:
            return False
        
        divisor = 3
        while divisor * divisor <= num:
            if num % divisor == 0:
                return False
            divisor += 2
        return True