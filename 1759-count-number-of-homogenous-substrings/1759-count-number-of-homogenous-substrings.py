class Solution:
    def countHomogenous(self, s: str) -> int:
        d=dict()
        unique=dict()
        i=0
        res=0
        while i<len(s):
            dum=s[i]
            c=s[i]
            if c not in unique:
                unique[c]=0
            while(i<len(s)-1 and c==s[i+1]):
                dum+=c
                i+=1
            d[dum]=d.get(dum,0)+1
            i+=1
        # print(d)

        for c in d:
            dum=c[0]
            n=len(c)
            count=(n*(n+1))//2
            res+=count*d[c]
            # print(res)
            
            
        return res%((10**9)+7)