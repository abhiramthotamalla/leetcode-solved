class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def help(i,dum):
            if(len(dum)>=2):
                res.append(dum.copy())
            if i==len(nums):
                return
            used=set()
            for p in range(i,len(nums)):
                if nums[p] in used:
                    continue
                if not dum or dum[-1]<=nums[p]:
                    used.add(nums[p])
                    dum.append(nums[p])
                    help(p+1,dum)
                    dum.pop()
                    
        help(0,[])
        return res