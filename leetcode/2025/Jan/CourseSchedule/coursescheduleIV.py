# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : coursescheduleIV.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/27 18:10
@Description: 
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(
            self, 
            numCourses: int, 
            prerequisites: List[List[int]], 
            queries: List[List[int]]
    ) -> List[bool]:
        adjList = defaultdict(list)
        inDegree = [0] * numCourses

        for u, v in prerequisites:
            adjList[u].append(v)
            inDegree[v] += 1  # Degree in 
        
        q = deque() # store the index of the node with inDegree = 0, which means it has no prerequisites
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        nodePrerequisites = defaultdict(set)
        while q:
            node = q.popleft()

            for adj in adjList[node]:
                nodePrerequisites[adj].add(node)
                for prereq in nodePrerequisites[node]:
                    nodePrerequisites[adj].add(prereq)
                
                inDegree[adj] -= 1
                if inDegree[adj] == 0:
                    q.append(adj)
        
        anwser = []
        for src, target in queries:
            anwser.append(src in nodePrerequisites[target])
        return anwser


    def checkIfPrerequisite_(
            self, numCourses: int, 
            prerequisites: List[List[int]], 
            queries: List[List[int]]
    ) -> List[bool]:
        
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]

        for u, v in prerequisites:
            isPrerequisite[u][v] = True
        
        for intermediate in range(numCourses):
            for src in range(numCourses):
                for target in range(numCourses):
                    isPrerequisite[src][target] = isPrerequisite[src][target] or (
                        isPrerequisite[src][intermediate] and
                        isPrerequisite[intermediate][target]
                    )
        anwser = []
        for src, target in queries:
            anwser.append(isPrerequisite[src][target])
        return anwser
        



if __name__ == '__main__':
    numCourses = 3
    prerequisites = [[1,2],[1,0],[2,0]]
    queries = [[1, 0], [1, 2]]

    s = Solution()
    s.checkIfPrerequisite(numCourses, prerequisites, queries)