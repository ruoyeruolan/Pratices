# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/03/02 11:01
@Description: 
"""

import heapq
from typing import List
from collections import defaultdict

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        # n1, n2 = len(nums1), len(nums2)
        dit = defaultdict(int)
        res = []

        for id, val in nums1:
            dit[id] += val
        
        for id, val in nums2:
            dit[id] += val
        
        for id in sorted(dit):
            if dit[id] != 0:
                res.append([id, dit[id]])
        return res
    
    def mergeArrays_(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        n1, n2 = len(nums1), len(nums2)
        p1, p2 = 0, 0

        res = []
        while p1 < n1 and p2 < n2:

            if nums1[p1][0] == nums2[p2][0]:
                res.append(
                    [
                        nums1[p1][0], nums1[p1][1] + nums2[p2][1]
                    ]
                )
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1
        
        while p1 < n1:
            res.append(nums1[p1])
            p1 += 1
        
        while p2 < n2:
            res.append(nums2[p2])
            p2 += 1
        return res



if __name__ == '__main__':

    nums1 = [[148,597],[165,623],[306,359],[349,566],[403,646],[420,381],[566,543],[730,209],[757,875],[788,208],[932,695]]
    nums2 = [[74,669],[87,399],[89,165],[99,749],[122,401],[138,16],[144,714],[148,206],[177,948],[211,653],[285,775],[309,289],[349,396],[386,831],[403,318],[405,119],[420,153],[468,433],[504,101],[566,128],[603,688],[618,628],[622,586],[641,46],[653,922],[672,772],[691,823],[693,900],[756,878],[757,952],[770,795],[806,118],[813,88],[919,501],[935,253],[982,385]]
