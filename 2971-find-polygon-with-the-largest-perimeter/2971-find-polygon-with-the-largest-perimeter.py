class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        res=-1
        total=0
        for k in nums:
            if total>k:
                res=total+k
            total+=k
        return res