class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        res=0
        for i in nums:
            res+=m-i
        return res