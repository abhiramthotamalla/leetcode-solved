class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=1
        s=[1 for i in range(len(nums))]
        for i in range(0,len(nums)-1):
            a=a*nums[i]
            s[i+1]=a
        a=1
        for i in range(len(nums)-1,0,-1):
            a=a*nums[i]
            s[i-1]=s[i-1]*a
        return s