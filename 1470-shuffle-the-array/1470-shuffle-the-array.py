class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        p,q=0,n
        res=[]
        for i in range(len(nums)):
            if(i%2==0):
                res.append(nums[p])
                p+=1
            else:
                res.append(nums[q])
                q+=1
        return res