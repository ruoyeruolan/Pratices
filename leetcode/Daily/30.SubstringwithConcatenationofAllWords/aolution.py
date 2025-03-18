# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : aolution.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/02/18 02:46
@Description: Hash Table
"""

from typing import List
from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        wordDict = defaultdict(int)
        res = []

        for word in words:
            wordDict[word] += 1  # if not in will insert the key and set the value to 0, so, we just add is fine
        
        for word, count in wordDict.items():
            if count == 5000:
                return [i for i in range(0, len(s) - 4999)]
        
        n = len(s)
        numWords = len(words)
        wordLength = len(words[0])
        totalLength = numWords * wordLength
        for k in range(wordLength):
            i = 0  # n-th word
            while i * wordLength + totalLength + k <= n:
                temp = wordDict.copy()
                j = numWords + i

                while j > i:
                    curWord = s[(j - 1) * wordLength + k:j * wordLength + k]
                    if curWord in temp:
                        temp[curWord] -= 1
                        if (temp[curWord] == 0):
                            del temp[curWord]
                        j -= 1
                        if (j == i):
                            res.append(i*wordLength + k)
                            i += 1
                            break
                    else:
                        i = j
                        break
        return res
