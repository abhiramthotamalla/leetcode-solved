class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row,col=len(matrix),len(matrix[0])
        for i in range(row):
            for j in range(col):
                if(i-1>=0 and j-1>=0):
                    if(matrix[i][j]==1):
                        matrix[i][j]=min(matrix[i-1][j],
                                        matrix[i][j-1],
                                        matrix[i-1][j-1])+1
        res=0
        for i in range(row):
            for j in range(col):
                res+=matrix[i][j]
                print(matrix[i][j],end=" ")
            print()
        
        return res