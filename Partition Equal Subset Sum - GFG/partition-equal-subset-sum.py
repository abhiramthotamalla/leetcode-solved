# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here
        if sum(arr)%2:
            return 0
        sum1=sum(arr)//2
        dp=[[False for i in range(sum1+1)] for j in range(N+1)]
        for i in range(N+1):
            dp[i][0]=True
        for i in range(1,N+1):
            for j in range(1,sum1+1):
                if(arr[i-1]<=j):
                    dp[i][j]=(dp[i-1][j-arr[i-1]] or dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[N][sum1]


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends