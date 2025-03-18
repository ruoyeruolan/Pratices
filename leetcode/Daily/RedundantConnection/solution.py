# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/29 16:54
@Description: 
"""

from typing import List

class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.cycleStart = -1

        n = len(edges)
        visited = [False] * n
        parent = [-1] * n
        adjList = [[] for _ in range(n)]  # Adjacency List

        for src, dest in edges:
            adjList[src - 1].append(dest - 1)  # `src - 1` and `dest - 1` to get the node index, as the nodes are 1-indexed
            adjList[dest - 1].append(src - 1)

        self.dfs(0, visited, adjList, parent)

        # cycleNodes = {}
        cycleNodes = [] 
        node = self.cycleStart
        while True:
            # cycleNodes[node] = 1
            cycleNodes.append(node)
            node = parent[node]

            if node == self.cycleStart:
                break
        
        for i in range(n - 1, -1, -1):
            if (edges[i][0] - 1) in cycleNodes and (edges[i][1] - 1) in cycleNodes:
                return edges[i]

    def dfs(self, src, visited, adjList, parent):
        visited[src] = True  # when enter this step, `src` node is visited

        for adj in adjList[src]:
            if not visited[adj]:
                parent[adj] = src
                self.dfs(adj, visited, adjList, parent)

            elif adj != parent[src] and self.cycleStart == -1:
                self.cycleStart = src
                parent[adj] = src


if __name__ == '__main__':
    edges = [[1,2],[1,3],[2,3]]
    s = Solution()
    s.findRedundantConnection(edges)