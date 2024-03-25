class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        for k in range(n):
            val=nums[k]
            if nums[abs(val)-1]<0:
                res.append(abs(val))
                continue
            nums[abs(val)-1]=-nums[abs(val)-1]
        return res