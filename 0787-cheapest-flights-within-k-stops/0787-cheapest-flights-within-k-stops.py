class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inf=float("inf")
        pri=[inf]*n
        pri[src]=0
        for i in range(k+1):
            dum=pri.copy()
            for s,d,p in flights:
                if pri[s]==inf:
                    continue
                if pri[s]+p<dum[d]:
                    dum[d]=p+pri[s]
            pri=dum
        return -1 if pri[dst]==inf else pri[dst]