from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key = lambda x:(x[0], x[1]))
        intervals.sort(key = lambda x:x[0])
        result = []
        s, e = intervals[0]
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
    

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key = lambda x:(x[0], x[1]))
        intervals.sort(key = lambda x:x[0])
        result = []
        
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        
        return result