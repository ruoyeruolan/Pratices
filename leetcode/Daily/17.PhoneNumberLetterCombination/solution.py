# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/14 04:59
@Description: 
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits: return []

        numberMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        def backtrace(index):
        
            if index == len(digits):
                combinations.append(''.join(combination))

            else:
                digit = digits[index]
                for letter in numberMap[digit]:
                    combination.append(letter)
                    backtrace(index + 1)
                    combination.pop()

        combination = []
        combinations = []
        backtrace(0)
        return combinations
