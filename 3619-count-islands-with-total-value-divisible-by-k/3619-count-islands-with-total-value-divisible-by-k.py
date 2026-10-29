class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        visit=set()
        res=0
        m,n=len(grid),len(grid[0])
        d=[-1,0,1,0,-1]
        
        def dfs(i,j):
            tot=grid[i][j]
            grid[i][j]=0
            for p in range(4):
                x,y=i+d[p],j+d[p+1]
                if 0<=x<m and 0<=y<n and grid[x][y]>0:
                    tot+=dfs(x,y)
            return tot
        
        return sum(grid[i][j]>0 and dfs(i,j)%k==0 for i in range(m) for j in range(n))