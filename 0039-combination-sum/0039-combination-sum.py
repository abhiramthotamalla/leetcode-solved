class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r=[]
        
        def dfs(i,c,total):
            if(total==target):
                r.append(c.copy())
                return 
            if(i>=len(candidates) or target<total):
                return
            c.append(candidates[i])
            dfs(i,c,total+candidates[i])
            c.pop()
            dfs(i+1,c,total)
        
        dfs(0,[],0)
        return r