class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1 for _ in range(len(nums))]
        maxi=1
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if(nums[i]<nums[j]):
                    dp[i]=max(dp[i],dp[j]+1)
                    maxi=max(maxi,dp[i])
        return maxi