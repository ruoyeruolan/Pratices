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


def findMedianSortedArrarys_(nums1: List[int], num2: List[int]) -> float:
    n, m = len(nums1), len(num2)
    if n > m:
        nums1, num2, n, m = num2, nums1, m, n
    imin, imax, half_len = 0, n, (n + m + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < n and num2[j-1] > nums1[i]:
            imin = i + 1
        elif i > 0 and nums1[i-1] > num2[j]:
            imax = i - 1
        else:
            if i == 0: max_of_left = num2[j-1]
            elif j == 0: max_of_left = nums1[i-1]
            else: max_of_left = max(nums1[i-1], num2[j-1])
            if (m + n) % 2 == 1:
                return max_of_left
            if i == n: min_of_right = num2[j]
            elif j == m: min_of_right = nums1[i]
            else: min_of_right = min(nums1[i], num2[j])
            return (max_of_left + min_of_right) / 2.0

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(findMedianSortedArrarys_(nums1, nums2))