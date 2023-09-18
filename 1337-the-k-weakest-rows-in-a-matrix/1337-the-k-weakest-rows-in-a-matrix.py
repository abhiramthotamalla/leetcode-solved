class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dum=[]
        for m in mat:
            dum.append(m.count(1))
        res=[]
        dum2=dum.copy()
        dum2.sort()
        for i in range(len(dum2)):
            if(k):
                idx=dum.index(dum2[i])
                res.append(idx)
                dum[idx]=-1
                k-=1
        return res