# -*- encoding: utf-8 -*-
"""
@Introduce  :
@File       : MedianofTwoSortedArrays.py
@Author     : ryrl
@email      : ryrl970311@gmail.com
@Time       : 2025/1/9 21:18
@Describe   :
"""
from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:

    nums1.extend(nums2)
    nums1.sort()
    n = len(nums1)
    if n % 2 == 0:
        return (nums1[n // 2] + nums1[n // 2 - 1]) / 2
    else:
        return nums1[n // 2]