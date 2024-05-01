from itertools import combinations
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n=len(candidates)
        res=[]
        exist=set()
        def combi(i,dum,dumSum):
            if target==dumSum:
                if str(dum) not in exist:
                    exist.add(str(dum.copy()))
                    res.append(dum.copy())
                    return
            if i>=n or target<dumSum:
                return

            dum.append(candidates[i])
            # print(dum)
            combi(i+1,dum,dumSum+candidates[i])
            dum.pop()
            val=candidates[i]
            while(i<n-1 and val==candidates[i+1]):
                i+=1
            combi(i+1,dum,dumSum)
            
        combi(0,[],0)
        # print(res)
        return res