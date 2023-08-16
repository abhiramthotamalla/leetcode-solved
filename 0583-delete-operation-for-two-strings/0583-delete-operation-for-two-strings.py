class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        text1=word1
        text2=word2
        dp=[[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        for i in range(len(text2)-1,-1,-1):
            for j in range(len(text1)-1,-1,-1):
                if(text2[i]==text1[j]):
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        firstcommon=len(word1)-dp[0][0]
        seconddiff=len(word2)-dp[0][0]
        return firstcommon+seconddiff