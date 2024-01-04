class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d=dict()
        for n in nums:
            d[n]=1+d.get(n,0)
        res=0
        for n in d:
            if d[n]<=1:
                return -1
            else:
                if d[n]%3==0:
                    res+=d[n]//3
                elif d[n]%3==1:
                    dum=(d[n]-4)//3
                    res+=dum+2
                elif d[n]%3==2:
                    dum=(d[n]-2)//3
                    res+=dum+1
        return res