class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[i for i in range(1,n+1)]
        res=[]
        def comb(i,dum,size):
            if i>n+1 or size>k:
                return
            if size==k:
                res.append(dum.copy())
                return
            #Take case
            dum.append(i)
            comb(i+1,dum,size+1)
            dum.pop()
            #Not take case
            comb(i+1,dum,size)
        
        dum=[]
        comb(1,dum,0)
        # print(*res)
        return res