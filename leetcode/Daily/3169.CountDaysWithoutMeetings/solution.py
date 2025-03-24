# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/24 17:52
# @Description: 

from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        meetings.sort()

        dys = 0
        lastes_end = 0

        for start, end in meetings:

            if start > lastes_end:
                dys += start - lastes_end - 1
            
            lastes_end = max(lastes_end, end)
        dys += days - lastes_end
        return dys



if __name__ == '__main__':

    days = 5
    meetings = [[2,4],[1,3]]

    s = Solution()
    s.countDays(days, meetings)

