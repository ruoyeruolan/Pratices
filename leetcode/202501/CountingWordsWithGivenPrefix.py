# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : CountingWordsWithGivenPrefix.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/10 01:09
@Description: 
"""
from typing import List


def prefixCount(words: List[str], pref: str) -> int:

    count = 0
    for word in words:
        if word.startswith(pref):
            count += 1
    return count

