# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/22 14:52
# @Description: 

import grp
from typing import List
from collections import defaultdict, deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)  # key: vertex, val: [vertex]

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        count = 0
        visited = set()

        def _dfs(curr: int, info: list) -> None:

            visited.add(curr)
            info[0] += 1
            info[1] += len(graph[curr])

            for node in graph[curr]:
                if node not in visited:
                    _dfs(node, info)
        
        for vertex in range(n):
            if vertex in visited:
                continue

            component_info = [0, 0]   # [node count, edge count]
            _dfs(vertex, component_info)

            if component_info[0] * (component_info[0] - 1) == component_info[1]:
                count += 1
        return count

    def bfs(self, n: int, edges:List[List[int]]) -> int:

        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        visited = [False] * n
        count = 0

        for vertex in range(n):
            if not visited[vertex]:
                component = []
                queue = [vertex]
                visited[vertex] = True

                while queue:
                    curr = queue.pop(0)
                    component.append(curr)

                    for neighbor in graph[curr]:
                        if not visited[neighbor]:
                            queue.append(neighbor)
                            visited[neighbor] = True
                
                isCompleted = True
                for node in component:
                    if len(graph[node]) != len(component) - 1:
                        isCompleted = False
                        break
                
                if isCompleted:
                    count += 1
        return count


if __name__ == '__main__':

    n = 6
    edges = [[0,1],[0,2],[1,2],[3,4]]

    s = Solution()
    s.countCompleteComponents(n, edges)