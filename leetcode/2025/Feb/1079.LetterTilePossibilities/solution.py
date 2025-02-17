# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : solution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/17 17:35
@Description: 
"""

from ast import List


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        sequence = set()
        used = [False] * len(tiles)

        self.generateSequences(tiles, '', used, sequence)
        return len(sequence) - 1

    def generateSequences(self, tiles: str, curr: str, used: list, sequence):
        sequence.add(curr)

        for idx in range(len(tiles)):  # for each iteration, all characters in tiles will be iterated
            if not used[idx]:
                used[idx] = True
                self.generateSequences(tiles, curr + tiles[idx], used, sequence)
                used[idx] = False
    
    def numTilePossibilities_(self, tiles: str) -> int:
        char_count = [0] * 26

        for char in tiles:
            char_count[ord(char) - ord('A')] += 1
        return self.findSequence(char_count)
    
    def findSequence(self, char_count: list) -> int:
        total = 0

        for pos in range(26):
            if char_count[pos] == 0:
                continue

            total += 1
            char_count[pos] -= 1
            total += self.findSequence(char_count)
            char_count[pos] += 1
        return total

if __name__ == '__main__':

    tiles = 'AAABBC'

    s = Solution()
    s.numTilePossibilities(tiles)