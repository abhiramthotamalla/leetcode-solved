class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        #condition max(l)<=min(r)
        maxi=[0 for i in range(len(nums))]
        mini=[0 for i in range(len(nums))]
        maxi[0]=nums[0]
        for i in range(1,len(nums)):
            maxi[i]=max(maxi[i-1],nums[i])
        mini[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            mini[i]=min(nums[i],mini[i+1])
        print(*maxi)
        print(*mini)
        for i in range(len(nums)):
            if(maxi[i]<=mini[i+1]):
                return i+1
        return 0