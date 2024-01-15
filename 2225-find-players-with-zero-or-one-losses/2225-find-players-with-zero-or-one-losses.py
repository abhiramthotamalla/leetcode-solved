class Solution(object):
    def findWinners(self, m):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        
        maxi=0
        for k in m:
            maxi=max(maxi,k[0],k[1])

        mark=[0 for i in range(maxi+1)]

        for k in m:
            mark[k[1]]-=1

        for k in m:
            if mark[k[0]]>=0:
                mark[k[0]]+=1
        out=[]
        win=[]
        for i in range(maxi+1):
            if mark[i]==-1:
                out.append(i)

            if mark[i]>0:
                win.append(i)
        return [win,out]