class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        winner=arr[0]
        c=0
        for i in range(1,len(arr)):
            if arr[i]>winner:
                c=1
                winner=arr[i]
            else:
                c+=1
            if c==k:
                return winner
        return winner