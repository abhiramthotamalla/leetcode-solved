class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res=0
        sum=0
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        print(nums)
        d=dict()
        d[0]=1
        for i in nums:
            if i-goal in d:
                res+=d[i-goal]
            d[i]=d.get(i,0)+1
        return res