class Solution:
    def minOperations(self, nums: List[int]) -> int:
        first=nums[0]
        count=0
        if len(nums)<=1:
            return 0
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                count+=1
                nums[i]+=1
            if nums[i-1]>nums[i]:
                diff=nums[i-1]-nums[i]+1
                count+=diff
                nums[i]+=diff
        return count