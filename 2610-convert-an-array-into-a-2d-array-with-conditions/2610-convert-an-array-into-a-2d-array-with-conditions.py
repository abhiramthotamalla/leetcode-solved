class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d=dict()
        for i in nums:
            d[i]=1+d.get(i,0)
        k1=d.values()
        
        nums.sort()
        maxi=0
        i=0
        while(i<len(nums)-1):
            c=0
            j=i+1
            while(j<len(nums)):
                if nums[i]==nums[j]:
                    c+=1
                    j+=1
                    maxi=max(c,maxi)
                else:
                    c=0
                    break
            i=j
            
        print(maxi)
        print(max(k1))
        
        res=[[] for i in range(maxi+1)]
        
        for v in d:
            c=0
            k=d[v]
            while(k and c<max(k1)):
                if v not in res[c]:
                    res[c].append(v)
                    k-=1
                c+=1
        return res