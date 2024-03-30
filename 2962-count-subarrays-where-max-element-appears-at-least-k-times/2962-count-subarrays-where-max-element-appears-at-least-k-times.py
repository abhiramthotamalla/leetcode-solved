class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi=max(nums)
        count,i=0,0
        res=0
        for j in range(len(nums)):
            if nums[j]==maxi:
                count+=1
            while(count==k):
                if nums[i]==maxi:
                    count-=1
                i+=1
            res+=i
        return res