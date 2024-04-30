class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor=nums[0]
        for i in nums[1:]:
            xor=xor^i
        xor=xor^k
        res=0
        while(xor):
            a=xor&1
            if a:
                res+=1
            xor=xor>>1
        return res