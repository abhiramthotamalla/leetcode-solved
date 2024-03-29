class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d=dict()
        i=0
        n=len(nums)
        maxl=0
        for j in range(n):
            d[nums[j]]=d.get(nums[j],0)+1
            while d[nums[j]]>k:
                d[nums[i]]-=1
                i+=1
            maxl=max(maxl,j-i+1)
        return maxl