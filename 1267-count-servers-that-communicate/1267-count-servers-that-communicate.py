class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res=0
        m,n=len(grid),len(grid[0])
        row,col=[0]*m,[0]*n
    
        for i in range(len(grid)):
            fr=0
            f=0
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    if fr==0 and f==0:
                        fr=j
                        f=1
                    else:
                        print(fr)
                        grid[i][fr]=-1
                        grid[i][j]=-1

        for i in range(len(grid[0])):
            fc=0
            f=0
            for j in range(len(grid)):
                if grid[j][i]==1 or grid[j][i]==-1:
                    if fc==0 and f==0:
                        fc=j
                        f+=1
                    else:
                        grid[j][i]=-1
                        grid[fc][i]=-1
        
        for i in range(len(grid)):
            print(grid[i])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==-1:
                    res+=1
        return res
                