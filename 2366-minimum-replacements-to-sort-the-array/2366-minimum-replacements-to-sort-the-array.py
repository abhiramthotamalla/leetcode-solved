import math
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        prev=nums[-1]
        for j in range(n-2,-1,-1):
            if(nums[j]<=prev):
                prev=nums[j]
                continue
            parts=(nums[j]+prev-1)//prev
            ans+=parts-1
            prev=nums[j]//parts
        return (ans)