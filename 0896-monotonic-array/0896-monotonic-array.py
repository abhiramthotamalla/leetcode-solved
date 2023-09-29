class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        stack=[]
        l=0
        for i in nums:
            while(stack and i<stack[-1]):
                stack.pop()
                l-=1
            stack.append(i)
            l+=1
        if l==len(nums):
            return True
        stack=[]
        l=0
        for i in nums:
            while(stack and i>stack[-1]):
                stack.pop()
                l-=1
            stack.append(i)
            l+=1
        if l==len(nums):
            return True
        return False