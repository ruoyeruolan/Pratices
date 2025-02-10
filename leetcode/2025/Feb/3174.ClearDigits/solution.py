# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/10 18:44
@Description: 
"""

class Solution:
    def clearDigits(self, s: str) -> str:
        
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        result = []
        for val in s:
            if val in digits and result:  # val.isdigit() and result
                result.pop()
            else:
                result.append(val)
        return ''.join(result)
                

if __name__ == '__main__':

    s = 'abc'
    s[0].isdigit()