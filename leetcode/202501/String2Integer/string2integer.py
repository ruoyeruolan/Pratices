# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : string2integer.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/10 18:04
@Description: 
"""

def myAtoi(s: str) -> int:

    s = s.strip()

    if not s:
        return 0
    
    if s[0] not in '+-0123456789':
        return 0
    
    res, sign = 0, 1
    for i in range(len(s)):
        if i == 0 and s[i] == '-':
            sign = -1

        elif i == 0 and s[i] == '+':
            sign = 1

        elif s[i] not in '0123456789':
            break
        
        else:
            res = res * 10 + int(s[i])
    
    res = res * sign
    if res < -2 **31:
        return -2 ** 31
    elif res > 2 ** 31 - 1:
        return 2 ** 31 - 1
    return res

if __name__ == '__main__':
    print(myAtoi('0-1'))
    print(myAtoi('42'))
    print(myAtoi('  -42'))
    print(myAtoi('A4193 with words'))
    print(myAtoi(' '))