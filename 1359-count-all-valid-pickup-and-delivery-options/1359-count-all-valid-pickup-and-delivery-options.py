class Solution:
    def countOrders(self, n: int) -> int:
        s=n*2
        res=1
        while(s>0):
            res*=(s-1)*s//2
            s-=2
        return res%(10**9+7)