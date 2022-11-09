class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right, s, e = [], [], 0, 1
        for interval in intervals:
            if interval[e] < newInterval[s]: 
                left.append(interval)
            elif newInterval[e] < interval[s]:
                right.append(interval)
            else:
                newInterval[s] = min(interval[s], newInterval[s])
                newInterval[e] = max(interval[e], newInterval[e])
        return left + [newInterval] + right
            