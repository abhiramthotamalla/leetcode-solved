class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n==1:
        #     return True
        # if n<=0 or n%4:
        #     return False
        # return self.isPowerOfFour(n/4)
        return n>0 and log(n,4)%1==0