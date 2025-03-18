# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/06 17:41
# @Description: 

from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        nrow = ncol = len(grid)

        temp = set()
        ans = []

        for row in range(nrow):
            for col in range(ncol):

                if grid[row][col] in temp:
                    ans.append(grid[row][col])
                temp.add(grid[row][col])
        
        temp_ = set([i for i in range(1, nrow ** 2 + 1)])
        ans.append((temp_ - temp).pop())
        return ans


if __name__ == '__main__':

    grid = [[9,1,7],[8,9,2],[3,4,6]]

    s = Solution()
    s.findMissingAndRepeatedValues(grid)

    

    
        