class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        s, e = 0, 1
        pe = intervals[0][e]
        remove = 0
        for i in range(1, len(intervals)):
            cur_s, cur_e = intervals[i]
            if pe > cur_s: #overlapping
                pe = min (pe, cur_e)
                remove += 1
            else:
                pe = cur_e
        return remove  