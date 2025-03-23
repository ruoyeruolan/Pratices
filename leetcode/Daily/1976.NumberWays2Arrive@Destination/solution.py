# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/23 15:48
# @Description: 

import heapq
from typing import List
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        graph = [[] for _ in range(n)]
        for src, dst, time in roads:
            graph[src].append((dst, time))
            graph[dst].append((src, time))
        
        min_heap = [(0, 0)] # time, dst
        shortest_time = [float('inf')] * n
        path_count = [0] * n

        shortest_time[0] = 0
        path_count[0] = 1

        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)

            if curr_time > shortest_time[curr_node]:
                continue

            for neighbor_node, road_time in graph[curr_node]:
                if curr_time + road_time < shortest_time[neighbor_node]:
                    shortest_time[neighbor_node] = curr_time + road_time
                    path_count[neighbor_node] = path_count[curr_node]
                    heapq.heappush(min_heap, (shortest_time[neighbor_node], neighbor_node))
                
                elif curr_time + road_time == shortest_time[neighbor_node]:
                    path_count[neighbor_node] = (
                        path_count[neighbor_node] + path_count[curr_node]
                    ) % MOD
        return path_count[n - 1]