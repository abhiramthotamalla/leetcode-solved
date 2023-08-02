class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp=[1 for i in range(5)]
        for i in range(2,n+1):
            for j in range(3,-1,-1):
                dp[j]+=dp[j+1]
        return sum(dp)