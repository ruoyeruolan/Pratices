# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : CountServersCommunicate.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/23 16:48
@Description: 
"""
# You are given a map of a server center, represented as a `m * n` integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
# Return the number of servers that communicate with any other server.

from typing import List
from collections import deque

class Solution:
    def countServers_brute_force(self, grid: List[List[int]]) -> int:
        numRows, numCols = len(grid), len(grid[0])
        communitcabeSeversCount = 0

        for row in range(numRows):
            for col in range(numCols):
                
                if grid[row][col] == 1:
                    canCommunicate = False
                    for otherCol in range(numRows):
                        if grid[otherCol][col] == 1 and otherCol != row:
                            canCommunicate = True
                            break
                    if canCommunicate:
                        communitcabeSeversCount += 1
                    else:
                        for otherRow in range(numCols):
                            if grid[row][otherRow] == 1 and otherRow != col:
                                canCommunicate = True
                                break
                        if canCommunicate:
                            communitcabeSeversCount += 1
        return communitcabeSeversCount
    
    def countServers_track(self, grid: List[List[int]]) -> int:
        numRows, numCols = len(grid), len(grid[0])
        rowCounts = [0] * numRows
        colCounts = [0] * numCols

        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == 1:
                    rowCounts[row] += 1
                    colCounts[col] += 1
                
        communitcabeSeversCount = 0
        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == 1 and (rowCounts[row] > 1 or colCounts[col] > 1):
                    communitcabeSeversCount += 1
        return communitcabeSeversCount
    
    def countServers(self, grid: List[List[int]]) -> int:

        count = 0
        numRows = len(grid)
        
        for row in range(numRows):
            s = sum(grid[row])
            if s > 1:
                count += s

            elif s == 1:
                col = grid[row].index(1)
                if sum(grid[i][col] for i in range(numRows)) > 1:
                    count += 1
        return count



if __name__ == '__main__':
    grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    ind = grid[1].index(1)
    grid[1][ind]