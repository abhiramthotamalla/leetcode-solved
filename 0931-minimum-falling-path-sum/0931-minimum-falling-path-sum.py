class Solution(object):
    def minFallingPathSum(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n=len(m)
        for i in range(1,n):
            for j in range(n):
                mid=m[i-1][j]
                left=m[i-1][j-1] if j>0 else float("inf")
                right=m[i-1][j+1] if j<n-1 else float("inf")
                m[i][j]=m[i][j]+min(left,right,mid)
                
        return min(m[-1])