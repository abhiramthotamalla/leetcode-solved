#User function Template for python3

def count(n):
    sum1=n
    nums=[3,5,10]
    N=len(nums)
    dp=[[0 for i in range(sum1+1)] for _ in range(N+1)]
            
    for i in range(N+1):
        dp[i][0]=1
    for i in range(1,N+1):
        for j in range(1,sum1+1):
            if(nums[i-1]<=j):
                dp[i][j]=(dp[i][j-nums[i-1]] + dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[N][sum1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(count(n))
        
# } Driver Code Ends