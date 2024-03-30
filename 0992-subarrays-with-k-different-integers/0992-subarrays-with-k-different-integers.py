class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        res=0
        d=defaultdict(int)
        near,far=0,0
        for r in range(len(nums)):
            d[nums[r]]+=1
            
            while(len(d)>k):
                d[nums[near]]-=1
                if d[nums[near]]==0:
                    d.pop(nums[near])
                near+=1
                far=near
                
            while(d[nums[near]]>1):
                d[nums[near]]-=1
                near+=1
            if len(d)==k:
                res+=near-far+1
        return res