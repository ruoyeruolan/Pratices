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
        if currIdx == len(result):  # if the idnex equal to the length of the result sequence, indicates all posion is filled
          return True
       
        if result[currIdx] != 0:  # if filled, go to next position
           return self.findLexicographicallyLargetSequence(currIdx + 1, result, isNumberUsed, target)
        
        for number2place in range(target, 0, -1):  # if not filled, try to fill the position by number (0, n]
            if isNumberUsed[number2place]:  # once or twice placement is completed in one iteration, so if the number is labeled as used, the number is nolonger accessiable.
               continue

            isNumberUsed[number2place] = True
            result[currIdx] = number2place  # The first time placement of a number

            if number2place == 1:
               if self.findLexicographicallyLargetSequence(currIdx + 1, result, isNumberUsed, target): # The number 1 just insert once, so if it cannot be inserted, just make the `isNumberUsed` and `result[currIdx]` back to the original status `0` and `False`
                  return True
            elif currIdx + number2place < len(result) and result[currIdx + number2place] == 0:
                
                result[currIdx + number2place] = number2place  # The second time placement of the number
                
                if self.findLexicographicallyLargetSequence(currIdx + 1, result, isNumberUsed, target):
                    return True
                result[currIdx + number2place] = 0
            
            result[currIdx] = 0  # if all operations above if failed, callback the status of the current index
            isNumberUsed[number2place] = False
        return False