class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if(sum(nums)%2):
            return False
        sum1=sum(nums)//2
        N=len(nums)
        dp=[[False for i in range(sum1+1)] for _ in range(N+1)]
        
        for i in range(N+1):
            dp[i][0]=True
        for i in range(1,N+1):
            for j in range(1,sum1+1):
                if(nums[i-1]<=j):
                    dp[i][j]=(dp[i-1][j-nums[i-1]] or dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
            
        return dp[N][sum1]