# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/16 17:40
# @Description: 

from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        low, high = 1, cars * cars * ranks[0]

        while low < high:

            mid = (low + high) // 2  # make all mechanics use the same time `mid`
            cars_repaired = sum(int((mid / rank) ** .5) for rank in ranks)

            if cars_repaired >= cars:
                high = mid
            else:
                low = mid + 1
        return low