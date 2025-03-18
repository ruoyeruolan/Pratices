# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/18 16:56
@Description: 
"""


class Solution:
    def smallestNumber(self, pattern: str) -> str:

        res = []
        num_stack = []

        for idx in range(len(pattern) + 1):

            num_stack.append(idx + 1)

            if idx == len(pattern) or pattern[idx] == 'I':
                while num_stack:
                    res.append(str(num_stack.pop()))
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    s.smallestNumber("IIIDIDDD")