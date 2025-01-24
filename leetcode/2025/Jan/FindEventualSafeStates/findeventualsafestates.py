# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : findeventualsafestates.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/24 17:11
@Description: 
"""

from typing import List
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        adj = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1
        
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        safeNodes = []
        for i in range(n):
            if safe[i]:
                safeNodes.append(i)
        return safeNodes


