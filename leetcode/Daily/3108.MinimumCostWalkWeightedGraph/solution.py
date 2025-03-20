# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/20 17:01
# @Description: 

from typing import List

from collections import deque

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        adj = [[] for _ in range(n)]
        for edge in edges:

            adj[edge[0]].append((edge[1], edge[2]))
            adj[edge[1]].append((edge[0], edge[2]))
        
        visited = [False] * n
        components = [0] * n
        
        component_cost = []
        component_id = 0
        for node in range(n):
            if not visited[node]:
                component_cost.append(
                    self.get_node_cost(node, adj, visited, components, component_id)
                )
                component_id += 1
        
        res = []
        for src, dst in query:
            if components[src] == components[dst]:
                res.append(component_cost[components[src]])
            else:
                res.append(-1)
        return res
    
    def get_node_cost(self, src, adj, visited, components, component_id):

        nodes_deque = deque()

        component_cost = -1

        nodes_deque.append(src)
        visited[src] = True

        while nodes_deque:
            node = nodes_deque.popleft()

            components[node] = component_id

            for neighbor, weight in adj[node]:
                component_cost &= weight

                if visited[neighbor]:
                    continue
                visited[neighbor] = True
                nodes_deque.append(neighbor)
        return component_cost
