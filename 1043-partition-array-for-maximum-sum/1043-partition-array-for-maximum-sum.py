class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)

        dp=[-1 for i in range(n+1)]
        for i in range(n-1,-1,-1):
            c=0
            maxi,res=-float("inf"),-float("inf")
            for j in range(i,min(i+k,n)):
                c+=1
                maxi=max(maxi,arr[j])
                
                dum=(c*maxi)+dp[j+1]
                res=max(res,dum)
            dp[i]=res
        return dp[0]+1