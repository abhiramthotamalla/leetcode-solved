class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=self.binSer(nums,target,True)
        r=self.binSer(nums,target,False)
        return [l,r]
    
    def binSer(self,nums,target,Left):
        i=0
        j=len(nums)-1
        p=-1
        while(i<=j):
            m=(i+j)//2
            if(target>nums[m]):
                i=m+1
            elif(target<nums[m]):
                j=m-1
            else:
                p=m
                if(Left):
                    j=m-1
                else:
                    i=m+1
        return p