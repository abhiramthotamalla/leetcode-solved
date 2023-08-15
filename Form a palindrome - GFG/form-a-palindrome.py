#User function Template for python3

class Solution:
    def findMinInsertions(self, S):
        text1=S
        text2=S[::-1]
        dp=[[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        for i in range(len(text2)-1,-1,-1):
            for j in range(len(text1)-1,-1,-1):
                if(text2[i]==text1[j]):
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return len(S)-dp[0][0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.findMinInsertions(S))
# } Driver Code Ends