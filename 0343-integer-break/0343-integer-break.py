class Solution:
    def integerBreak(self, n: int) -> int:
        res=[0,1,1,2,4]
        if n<=4:
            return res[n]
        res[2]=2
        for i in range(5,n+1):
            maxi=0
            for p in range(i-1,0,-1):
                maxi=max(maxi,(p)*res[i-p])
                if i==p+p:
                    maxi=max(maxi,p*p)
            res.append(maxi)
        return res[-1]