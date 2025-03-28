# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/28 17:34
# @Description: 

import heapq
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
        nrow, ncol = len(grid), len(grid[0])
        res = [0] * len(queries)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queries_sorted = sorted((val, idx) for idx, val in enumerate(queries))

        visited = [[False] * ncol for _ in range(nrow)]
        heap = [(grid[0][0], 0, 0)]  # (val, row, col)
        heapq.heapify(heap)

        count = 0
        visited[0][0] = True

        for val, idx in queries_sorted:

            while heap and heap[0][0] < val:
                _, row, col = heapq.heappop(heap)
                count += 1

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < nrow and 0 <= nc < ncol and not visited[nr][nc]:
                        visited[nr][nc] = True
                        heapq.heappush(heap, (grid[nr][nc], nr, nc))
            res[idx] = count
        return res

    