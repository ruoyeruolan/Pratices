# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/28 21:42
@Description: 
"""

from typing import List
from collections import deque

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        numRow, numCol = len(grid), len(grid[0])
        visited = [[False for _ in range(numCol)] for _ in range(numRow)]

        result = 0
        for row in range(numRow):
            for col in range(numCol):
                if grid[row][col] and not visited[row][col]:
                    result = max(result, self.countFish(grid, visited, row, col))
        return result
    
    def countFish(self, grid, visited, row: int, col: int):
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        numRow, numCol = len(grid), len(grid[0])
        numFish = 0
        q = [(row, col)]
        visited[row][col] = True

        while q:
            row, col = q.pop(0)
            numFish += grid[row][col]

            for d in range(4):
                row_ = row + dx[d]
                col_ = col + dy[d]
                
                if self.isVaild(row_, col_, numRow, numCol, grid, visited):
                    q.append((row_, col_))
                    visited[row_][col_] = True
        return numFish
    
    def isVaild(self, x, y, nrow, ncol, grid, visited):
        return 0 <= x < nrow and 0 <= y < ncol and grid[x][y] and not visited[x][y]
    
    def dfs(self, grid, row, col):  # TODO: This is the optimal solution
        nrow, ncol = len(grid), len(grid[0])
        if row < 0 or col < 0 or row >= nrow or col >= ncol:
            return 0
        
        if grid[row][col] == 0:
            return 0
        temp = grid[row][col]
        grid[row][col] = 0
        return temp + self.dfs(grid, row + 1, col) + self.dfs(grid, row - 1, col) + \
            self.dfs(grid, row, col + 1) + self.dfs(grid, row, col - 1)


if __name__ == '__main__':
    # grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
    grid = [[0,5],[8,4]]
    s = Solution()
    s.findMaxFish(grid)