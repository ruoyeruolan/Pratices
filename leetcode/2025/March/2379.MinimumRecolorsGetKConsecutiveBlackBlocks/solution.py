# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/08 16:02
# @Description: 

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        n = len(blocks)

        left = num_white = 0
        recolors = 100

        for right in range(n):

            if blocks[right] == 'W':
                num_white += 1
            
            if right - left + 1 == k:
                recolors = min(recolors, num_white)
            
                if blocks[left] == 'W':
                    num_white -= 1

                left += 1
        return recolors