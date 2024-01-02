class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d=dict()
        for i in nums:
            d[i]=1+d.get(i,0)
        k1=d.values()
        
        res=[[] for i in range(max(k1))]
        
        for v in d:
            c=0
            k=d[v]
            while(k and c<max(k1)):
                if v not in res[c]:
                    res[c].append(v)
                    k-=1
                c+=1
            
        
        
        return res