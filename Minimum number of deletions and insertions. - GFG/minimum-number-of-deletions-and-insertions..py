#User function Template for python3
class Solution:
	def minOperations(self, s1, s2):
	    text1=s1
        text2=s2
        dp=[[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        for i in range(len(text2)-1,-1,-1):
            for j in range(len(text1)-1,-1,-1):
                if(text2[i]==text1[j]):
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        firstcommon=len(s1)-dp[0][0]
        seconddiff=len(s2)-dp[0][0]
        return firstcommon+seconddiff


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s1,s2 = input().split()
		ob = Solution()
		ans = ob.minOperations(s1,s2)
		print(ans)
# } Driver Code Ends