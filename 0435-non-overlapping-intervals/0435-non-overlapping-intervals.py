class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda p:p[0])
        prevEnd=intervals[0][1]
        res=0
        for start,end in intervals[1:]:
            if start>=prevEnd:
                prevEnd=end
            else:
                res+=1
                prevEnd=min(end,prevEnd)
        return res