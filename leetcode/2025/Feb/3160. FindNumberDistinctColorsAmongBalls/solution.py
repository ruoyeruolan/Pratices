# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/07 17:42
@Description: 
"""

from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        colorMap = {}
        ballMap = {}
        result = []
        
        for ball, color in queries:

            if ball in ballMap:

                pcolor = ballMap[ball]
                colorMap[pcolor] -= 1

                if colorMap[pcolor] == 0:
                    del colorMap[pcolor]
            
            ballMap[ball] = color
            colorMap[color] = colorMap.get(color, 0) + 1
            result.append(len(colorMap))
        return result
     
            
if __name__ == '__main__':

    limit = 1
    # queries = [[1,4],[2,5],[1,3],[3,4]]
    # queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
    queries = [[0,1],[0,4],[1,2],[1,5],[1,4]]
    
    s = Solution()
    s.queryResults(limit, queries)