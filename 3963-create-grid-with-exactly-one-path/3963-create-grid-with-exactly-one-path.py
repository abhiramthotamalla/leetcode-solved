class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        l=[["#" for i in range(n)] for i in range(m)]
        
        for i in range(m):
            l[i][0]="."
        for i in range(n):
            l[-1][i]="."
        for i in range(m):
            l[i]="".join(l[i])
        return l