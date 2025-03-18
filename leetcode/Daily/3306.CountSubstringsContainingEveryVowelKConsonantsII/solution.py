# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/10 17:25
# @Description: 

from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.atLeastK(word, k) - self.atLeastK(word, k + 1)

    def isVowel(self, x: str) -> bool:
        return x in ['a', 'e', 'i', 'o', 'u']
    
    def atLeastK(self, word: str, k: int) -> int:

        num_vaild_substrings = 0
        start = end = 0

        vowel_count = defaultdict(int)
        consonant_count = 0

        while end < len(word):

            letter = word[end]

            if self.isVowel(letter):
                vowel_count[letter] += 1
            else:
                consonant_count += 1

            while len(vowel_count) == 5 and consonant_count >= k:
                num_vaild_substrings += len(word) - end
                start_letter = word[start]

                if self.isVowel(start_letter):
                    vowel_count[start_letter] -= 1

                    if vowel_count[start_letter] == 0:
                        vowel_count.pop(start_letter)
                else:
                    consonant_count -= 1
                start += 1
            end += 1
        return num_vaild_substrings
