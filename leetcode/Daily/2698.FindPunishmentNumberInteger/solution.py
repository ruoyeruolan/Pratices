# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/15 16:34
@Description: 
"""

class Solution:
    def punishmentNumber(self, n: int) -> int:
        punishmentNum = 0
        for cnum in range(1, n + 1):
            squareNum = cnum * cnum

            if self.canPartition_(squareNum, cnum):
                punishmentNum += squareNum
            # stringNum = str(squareNum)
            # if self.canPartition(stringNum, cnum):
            #     punishmentNum += squareNum

            # memo = [[-1] * (cnum + 1) for _ in range(len(stringNum))]

            # if self.findPartitions(0, 0, cnum, stringNum, memo):
            #     punishmentNum += squareNum
        return punishmentNum

    def findPartitions(self, startIndex, csum, target, stringNum, memo) -> bool:

        if startIndex == len(stringNum): return csum == target
        
        if csum > target: return False

        if memo[startIndex][csum] != -1: return memo[startIndex][csum]

        partitionFound = False
        for cidx in range(startIndex, len(stringNum)):
            cstring = stringNum[startIndex : cidx + 1]
            cnum = int(cstring)

            partitionFound = partitionFound or self.findPartitions(
                cidx + 1,
                csum + cnum,
                target,
                stringNum,
                memo
            )

            if partitionFound:
                memo[startIndex][csum] = True
                return True
        
        memo[startIndex][csum] = 0
        return False

    def canPartition(self, stringNum: str, target: int) -> bool:

        if not stringNum and target == 0: return True

        if target < 0: return False

        for cidx in range(len(stringNum)):
            left = stringNum[:cidx + 1]
            right = stringNum[cidx + 1 :]

            if self.canPartition(right, target - int(left)):
                return True
        return False
    
    def canPartition_(self, num: int, target: int) -> bool:

        if target < 0 or num < target: return False

        if num == target: return True

        return (
            self.canPartition_(num // 10, target - num % 10) or
            self.canPartition_(num // 100, target - num % 100) or
            self.canPartition_(num // 1000, target - num % 1000)
        )
