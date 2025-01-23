# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : maphighestpeak.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/22 18:05
@Description: BSF & DP 
"""
# You are given an integer matrix isWater of size m x n that represents a map of land and water cells.
# If isWater[i][j] == 0, cell (i, j) is a land cell.
# If isWater[i][j] == 1, cell (i, j) is a water cell.
# You must assign each cell a height in a way that follows these rules:
# The height of each cell must be non-negative.
# If the cell is a water cell, its height must be 0.
# Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
# Find an assignment of heights such that the maximum height in the matrix is maximized.
# Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

# Example 1:
# Input: isWater = [[0,1],[0,0]]
# Output: [[1,0],[2,1]]
# Explanation: The image shows the assigned heights of each cell.
# The blue cell is the water cell, and the green cells are the land cells.

# Example 2:
# Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
# Output: [[1,1,0],[0,1,1],[1,2,2]]
# Explanation: A height of 2 is the maximum possible height of any assignment.
# Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.
 

from typing import List
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        nrow, ncol = len(isWater), len(isWater[0])
        cellHeights = [[-1 for _ in range(ncol)] for _ in range(nrow)]

        queue = deque()
        for row in range(nrow):
            for col in range(ncol):
                if isWater[row][col] == 1:
                    queue.append((row, col))
                    cellHeights[row][col] = 0
        
        heightOfNextLayer = 1
        while queue:
            layersize = len(queue)

            for _ in range(layersize):
                row, col = queue.popleft()

                for d in range(4):
                    neighborRow = row + dx[d]
                    neighborCol = col + dy[d]

                    if self._is_vaild_cell(neighborRow, neighborCol, nrow, ncol) \
                        and cellHeights[neighborRow][neighborCol] == -1:
                        cellHeights[neighborRow][neighborCol] = heightOfNextLayer
                        queue.append((neighborRow, neighborCol))
            heightOfNextLayer += 1
        return cellHeights
                        
    
    def _is_vaild_cell(self, x, y, nrow, ncol):
        return 0 <= x < nrow and 0 <= y < ncol
