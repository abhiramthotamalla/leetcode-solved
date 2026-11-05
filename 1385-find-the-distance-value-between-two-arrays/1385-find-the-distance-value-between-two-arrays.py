class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, k):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        res=0
        for i in arr1:
            if all(abs(i-j)>k for j in arr2):
                res+=1
        return res