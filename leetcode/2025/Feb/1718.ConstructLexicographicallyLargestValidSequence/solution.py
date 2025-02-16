# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/16 17:42
@Description: 
"""

from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        
       result = [0] * (n * 2 - 1)
       isNumberUsed = [False] * (n + 1)

       self.findLexicographicallyLargetSequence(0, result, isNumberUsed, n)
       return result
    
    def findLexicographicallyLargetSequence(self, currIdx, result, isNumberUsed, target) -> bool:
        if currIdx == len(result):
          return True
       
        if result[currIdx] != 0:
           return self.findLexicographicallyLargetSequence(currIdx + 1, result, isNumberUsed, target)
        
        for number2place in range(target, 0, -1):
            if isNumberUsed[number2place]:
               continue

            isNumberUsed[number2place] = True
            result[currIdx] = number2place

            if number2place == 1:
               if self.findLexicographicallyLargetSequence(currIdx + 1, result, isNumberUsed, target):
                  return True
            elif currIdx + number2place < len(result) and result[currIdx + number2place] == 0:
                
                result[currIdx + number2place] = number2place
                
                if self.findLexicographicallyLargetSequence(currIdx + 1, result, isNumberUsed, target):
                    return True
                result[currIdx + number2place] = 0
            
            result[currIdx] = 0
            isNumberUsed[number2place] = False
        return False