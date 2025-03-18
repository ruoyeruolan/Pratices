# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/08 18:24
@Description: 
"""

from collections import defaultdict
import heapq


class NumberContainers:

    def __init__(self):
       self.number2index = defaultdict(list)
       self.index2number = {}

    def change(self, index: int, number: int) -> None:
        self.index2number[index] = number

        heapq.heappush(self.number2index[number], index)
        

    def find(self, number: int) -> int:
        
        if not self.number2index[number]:
            return -1
        
        while self.number2index[number]:

            index = self.number2index[number][0]

            if self.index2number[index] == number:
                return index
            
            heapq.heappop(self.number2index[number])
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)