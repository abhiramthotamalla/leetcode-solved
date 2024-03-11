class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count=collections.Counter(s)
        res=[]
        for k in order:
            if k in count:
                dum=k*count[k]
                res.append(dum)
                del count[k]
        for c,k in count.items():
            dum=c*k
            res.append(dum)
        return "".join(res)