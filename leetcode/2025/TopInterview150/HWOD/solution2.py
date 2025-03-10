
from typing import List
from collections import defaultdict


class Solution:

    def getWorkers(self, array: List[int], num: int):

        hashMap = defaultdict(list)

        for i in array:
            if i in [0, 1, 2, 3]:
                hashMap[0].append(i)
            else:
                hashMap[1].append(i)
        
        if num == 1:
             if len(hashMap[0]) == 0:
                 
             if len(hashMap[0]) <= len(hashMap[1]):
                 return hashMap[0]
             else:
                 return hashMap[1]
        
        if num == 2:
            pass