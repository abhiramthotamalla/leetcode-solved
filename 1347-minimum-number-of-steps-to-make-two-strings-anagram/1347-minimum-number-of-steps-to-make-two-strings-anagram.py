class Solution:
    def minSteps(self, s: str, t: str) -> int:
        n=len(s)
        same=0
        ds=dict()
        for c in s:
            ds[c]=ds.get(c,0)+1
            
        dt=dict()
        for c in t:
            dt[c]=dt.get(c,0)+1
            
        for c in dt:
            if c in s:
                same+=min(ds[c],dt[c])
        # print(same)
        # print(dt,ds)
        return n-same