class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            arr.sort()
            for i in range(1,len(arr)-1):
                if(arr[i]-arr[i-1]!=arr[i+1]-arr[i]):
                    return False
            return True
        res=[]
        for i in range(len(l)):
            res.append(check(nums[l[i]:r[i]+1]))
        return res