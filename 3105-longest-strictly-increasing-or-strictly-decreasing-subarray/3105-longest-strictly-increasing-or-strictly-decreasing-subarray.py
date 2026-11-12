class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res=0
        cm=0
        c=0
        for i in nums:
            if cm<i:
                cm=i
                c+=1
            else:
                cm,c=i,1
            res=max(c,res)
            # print(cm,c)
        print("r to l")
        c=0
        cm=0
        for i in range(len(nums)-1,-1,-1):
            if cm<nums[i]:
                cm=nums[i]
                c+=1
            else:
                cm,c=nums[i],1
            res=max(c,res)
            # print(cm,c)
        return res