#User function Template for python3

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        dp=[[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if(S1[i-1]==S2[j-1]):
                    dp[i-1][j-1]=1+dp[i-2][j-2]
                else:
                    dp[i-1][j-1]=0
        maxi=float("-inf")
        for i in range(n):
            for j in range(m):
                maxi=max(maxi,dp[i][j])
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends