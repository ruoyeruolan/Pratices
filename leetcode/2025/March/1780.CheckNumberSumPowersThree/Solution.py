# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : Solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/04 18:29
# @Description: 

from aiohttp import ServerTimeoutError


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        while n > 0:

            if n % 3 == 2:
                return False
            n //= 3
        return True
    
    def checkPowersOfThree_(self, n: int) -> bool:
        return self.helper(n, 0)

    def helper(self, n: int, power: int) -> bool:

        if n == 0:
            return True
        
        if 3 ** power > n:
            return False
        
        # add_power = self.helper(n - 3 ** power, power + 1)
        # skip_power = self.helper(n, power + 1)
        return self.helper(n - 3 ** power, power + 1) or self.helper(n, power + 1)