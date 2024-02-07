from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        s, e = newInterval

        for interval in intervals:
            if interval[1] < s:
                result.append(interval)
            elif interval[0] > e:
                result.append([s, e])
                s, e = interval
            else:
                s = min(interval[0], s)
                e = max(interval[1], e)
        result.append([s, e])
        return result

