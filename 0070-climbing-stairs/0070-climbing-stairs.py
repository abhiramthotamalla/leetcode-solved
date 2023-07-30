class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #climbing stairs using dynamic programming
        a,b=1,1
        for i in range(n-1):
            t=a
            a=a+b
            b=t
        return a