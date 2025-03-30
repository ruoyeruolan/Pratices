# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/30 15:48
# @Description: 

from typing import List
from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        maxIndex4Letters = defaultdict(int)
        for idx, val in enumerate(s):
            maxIndex4Letters[val] = idx
        
        res = []
        start = end = 0

        for idx, chr in enumerate(s):
            end = max(end, maxIndex4Letters[chr])

            if idx == end:
                res.append(idx - start + 1)
                start = idx + 1
        return res
