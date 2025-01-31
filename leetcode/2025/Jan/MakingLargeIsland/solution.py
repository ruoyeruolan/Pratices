# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/31 16:02
@Description: 
"""

from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        islandSize = {}
        islandId = 2

        nrow, ncol = len(grid), len(grid[0])

        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == 1:
                    islandSize[islandId] = self.exploreIsland(grid, islandId, row, col)
                    islandId += 1
        
        if not islandSize:
            return 1  # if all 0, flip 0 to 1 will create a island, so return 1
        
        if len(islandSize) == 1:
            islandId -= 1
            size = islandSize[islandId]
            return size if size == nrow * ncol else size + 1  # if the only island is the whole grid, dn't need to flip any 0 to 1, return size, otherwise, return size + 1
        
        maxIslandSize = 1
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == 0:
                    cislandSize = 1
                    neighboringIslands = set()

                    if row + 1 < nrow and grid[row + 1][col] > 1:
                        neighboringIslands.add(grid[row + 1][col])
                    
                    if row - 1 >= 0 and grid[row - 1][col] > 1:
                        neighboringIslands.add(grid[row - 1][col])
                    
                    if col + 1 < ncol and grid[row][col + 1] > 1:
                        neighboringIslands.add(grid[row][col + 1])
                    
                    if col - 1 >= 0 and grid[row][col - 1] > 1:
                        neighboringIslands.add(grid[row][col - 1])
                    
                    for islandId in neighboringIslands:
                        cislandSize += islandSize[islandId]
                    maxIslandSize = max(maxIslandSize, cislandSize)
        return maxIslandSize


    def exploreIsland(self, grid: List[List[int]], islandId: int, crow: int, ccol: int) -> int:
        
        if crow < 0 or ccol < 0 or crow >= len(grid) or ccol >= len(grid[0]) or grid[crow][ccol] != 1:
            return 0
        
        grid[crow][ccol] = islandId  # mark the cell as visited by the island ID
        return (
            1 + # current cell
            self.exploreIsland(grid, islandId, crow - 1, ccol) + 
            self.exploreIsland(grid, islandId, crow + 1, ccol) + 
            self.exploreIsland(grid, islandId, crow, ccol - 1) + 
            self.exploreIsland(grid, islandId, crow, ccol + 1)  # cell connected to current cell
        )