class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda p:p[0])
        res=[]
        res.append(intervals[0])
        
        for i in range(1,len(intervals)):
            stackEnd=res[-1][1]
            if(stackEnd<intervals[i][0]):
                res.append(intervals[i])
            else:
                res[-1][1]=max(res[-1][1],intervals[i][1])
            
        return res