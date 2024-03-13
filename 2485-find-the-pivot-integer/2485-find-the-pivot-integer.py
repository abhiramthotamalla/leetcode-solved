class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        dp=[i for i in range(n+1)]
        for i in range(1,n+1):
            dp[i]=dp[i-1]+i
        # print(*dp)
        for i in range(1,n):
            if dp[i-1]==dp[-1]-dp[i]:
                return i
        return -1