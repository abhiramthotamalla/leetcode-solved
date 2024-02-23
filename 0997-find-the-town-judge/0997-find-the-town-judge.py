class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
        t=dict()
        for l in trust:
            t[l[1]]=t.get(l[1],0)+1
        for l in range(1,n+1):
            t[l]=t.get(l,0)
        s=set()
        for l in trust:
            s.add(l[0])
        for k in t:
            if t[k]==n-1 and k not in s:
                return k
        return -1