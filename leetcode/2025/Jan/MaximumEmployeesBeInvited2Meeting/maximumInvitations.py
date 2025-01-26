# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : maximumInvitations.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/26 20:34
@Description: 
"""

from typing import List
from collections import deque

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        reversedGraph = [[] for _ in range(n)]

        for idx in range(n):
            reversedGraph[favorite[idx]].append(idx)
        
        longestCycle = 0
        twoCycleInvitations = 0
        
        visited = [False] * n
        for idx in range(n):
            if not visited[idx]:
                visitedPersons = {}
                idx_current = idx
                distance = 0

                while True:
                    if visited[idx_current]:
                        break
                    
                    visited[idx_current] = True
                    visitedPersons[idx_current] = distance
                    distance += 1
                    idx_next = favorite[idx_current]

                    if idx_next in visitedPersons:
                        cycleLength = distance - visitedPersons[idx_next]
                        longestCycle = max(longestCycle, cycleLength)

                        if cycleLength == 2:
                            visitedNodes = {idx_current, idx_next}
                            twoCycleInvitations += (
                                2 + 
                                self.bfs(idx_next, visitedNodes, reversedGraph) + 
                                self.bfs(idx_current, visitedNodes, reversedGraph) 
                            )
                        break
                    idx_current = idx_next
        return max(longestCycle, twoCycleInvitations)

    def bfs(self, start_node: int, visited_nodes: set, reversedGraph: List[List[int]]) -> int:
        queue = deque([(start_node, 0)])
        max_distance = 0

        while queue:
            node, distance = queue.popleft()

            for neighbor in reversedGraph[node]:
                if neighbor in visited_nodes:
                    continue
                visited_nodes.add(neighbor)
                queue.append((neighbor, distance + 1))
                max_distance = max(max_distance, distance + 1)
        return max_distance