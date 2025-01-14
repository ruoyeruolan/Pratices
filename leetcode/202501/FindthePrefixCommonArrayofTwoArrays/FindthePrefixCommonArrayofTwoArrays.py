# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : FindthePrefixCommonArrayofTwoArrays.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/14 11:53
@Description: 
"""

# You are given two **0-indexed** integer permutations `A` and `B` of length `n`.
# A prefix common array of `A` and `B` is an array `C` such that `C[i]` is equal to the count of numbers that are present at or before the index `i` in both `A` and `B`.
# Return the **prefix common array** of `A` and `B`.
# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

# Example 1:
# Input: A = [1,3,2,4], B = [3,1,2,4]
# Output: [0,2,3,4]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
# At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
# Example 2:

# Input: A = [2,3,1], B = [3,1,2]
# Output: [0,1,3]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: only 3 is common in A and B, so C[1] = 1.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.

from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = [0] * len(A)

        for i in range(len(A)):
            C[i] = len(set(A[:i+1]).intersection(B[:i+1]))
        return C
    
    def findThePrefixCommonArray_(self, A: List[int], B: List[int]) -> List[int]:
        length = len(A)
        res = [0] * length
        freq = [0] * length + 1
        common_count = 0
        
        for i in range(length):
            
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common_count += 1
            
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common_count += 1

            res[i] = common_count
        return res



if __name__ == '__main__':
   A = [1,3,2,4]
   B = [3,1,2,4]
   [0] * 4
   A.sort() & B.sort()
   len(set(A[:3+1]).intersection(B[:3+1]))