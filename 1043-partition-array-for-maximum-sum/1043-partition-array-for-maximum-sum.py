class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[-1 for i in range(n)]
        def helper(idx,nums,k):
            n=len(nums)

            if(idx==n):
                return 0
            if dp[idx]!=-1:
                return dp[idx]
            maxi=-float("inf")
            res=-float("inf")
            c=0
            for i in range(idx,min(n,idx+k)):
                c+=1
                maxi=max(maxi,nums[i])
                dum=(c*maxi)+helper(idx+c,nums,k)
                res=max(res,dum)
            dp[idx]=res
            return dp[idx]
        return helper(0,arr,k)