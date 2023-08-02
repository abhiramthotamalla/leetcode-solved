class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp=[[0 for i in range(5)] for _ in range(n+1)]
        for i in reversed(range(n+1)):
            trace=0
            for j in reversed(range(5)):
                if(i==n):
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i+1][j]+trace
                    trace=dp[i][j]
        return dp[0][0]