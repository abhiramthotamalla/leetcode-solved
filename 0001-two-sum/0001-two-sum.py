class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a=[]
        d={}
        for i in range(len(nums)):
            if(target-nums[i] in d):
                a.append(d[target-nums[i]])
                #d[nums[i]]=i
                a.append(i)
                return a
            d[nums[i]]=i