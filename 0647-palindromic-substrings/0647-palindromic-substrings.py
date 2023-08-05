class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        c=0
        dp=[[False for i in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i]=True
            c+=1
        for i in range(n-1):
            if(s[i]==s[i+1]):
                c+=1
                dp[i][i+1]=True
        for k in range(3,n+1):
            for i in range(n-k+1):
                j=k+i-1
                if(s[i]==s[j] and dp[i+1][j-1]):
                    c+=1
                    dp[i][j]=True
        #print(*dp)
        return c