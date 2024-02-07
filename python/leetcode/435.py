from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        n = len(intervals)
        result = 0
        s, e = intervals[0]
        for i in range(1, n):
            if e > intervals[i][0]:
                result += 1
            else:
                s, e = intervals[i]
        return result