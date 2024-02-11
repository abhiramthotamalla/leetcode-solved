class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp=[0 for i in range(n+1)]
        i=0
        while(i*i<=n):
            dp[i*i]=1
            i+=1
        
        # dp[0]=0
        for tar in range(1,n+1):
            if dp[tar]==1:
                continue
            root=int(math.sqrt(tar))
            res=float("inf")
            for i in range(1,root+1):
                res=min(res,dp[i*i]+dp[tar-(i*i)])
            dp[tar]=res
        return dp[n]