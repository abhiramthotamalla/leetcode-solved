class Solution:
    def countHomogenous(self, s: str) -> int:
        mod=(10**9)+7
        res=0
        for i,j in groupby(s):
            n=len(list(j))
            res+=(n*(n+1))//2
            res%=mod
        return res%mod