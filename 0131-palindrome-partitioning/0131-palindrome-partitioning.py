class Solution:
    def partition(self, s: str) -> List[List[str]]:
        part=[]
        res=[]
        n=len(s)
        def isPali(s,i,j):
            while(i<=j):
                if(s[i]!=s[j]):
                    return False
                i+=1
                j-=1
            return True
        def dfs(i):
            if i>=n:
                res.append(part.copy())
                return
            for j in range(i,n):
                if(isPali(s,i,j)):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res