class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recPre(idx,nums,sol):
            if(idx==len(nums)):
                ds=list(nums)
                if(ds not in sol):
                    sol.append(ds)
                return 
            for i in range(len(nums)):
                swap(i,idx,nums)
                recPre(idx+1,nums,sol)
                swap(i,idx,nums)
        def swap(i,j,nums):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        sol=[]
        recPre(0,nums,sol)
        return sol