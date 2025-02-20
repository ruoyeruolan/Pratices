# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/20 18:19
@Description: 
"""

from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        n = len(nums)
        res = []

        for idx in range(n):
            
            temp = nums[idx][idx]
            res.append('1' if temp == '0' else '0')
        return ''.join(res)

    def findDifferentBinaryString_(self, nums: List[str]) -> str:
        return self.generate('', nums)

    def generate(self, curr: str, nums: List[str]):

        if len(curr) == len(nums):
            if curr not in nums:
                return curr
            return ''
        
        add_zero = self.generate(curr + '0', nums)
        if add_zero:
            return add_zero
        return self.generate(curr + '1', nums)

if __name__ == '__main__':

    nums = ["01","10"]
    s = Solution()
    s.findDifferentBinaryString(nums)
    