# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/25 18:21
# @Description: 

from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        return self.check_cuts(rectangles, 0) or self.check_cuts(rectangles, 1)

    def check_cuts(self, rectangles: List[List[int]], dim: int) -> bool:

        gaps = 0

        rectangles.sort(key=lambda rec: rec[dim])

        furthest_end = rectangles[0][dim + 2]

        for idx in range(1, len(rectangles)):
            rec = rectangles[idx]

            if furthest_end <= rec[dim]:
                gaps += 1
            
            furthest_end = max(furthest_end, rec[dim + 2])
        return gaps >= 2