class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        d={}
        res=0
        for i in range(len(nums)):
            if nums[i]-k in d:
                res+=d[nums[i]-k]
            if nums[i]+k in d:
                res+=d[nums[i]+k]
            d[nums[i]]=d.get(nums[i],0)+1
        return res