class Solution:
    def minDeletions(self, s: str) -> int:
        d=dict()
        for i in s:
            d[i]=1+d.get(i,0)
        arr=list(d.values())
        arr.sort()
        ch=[0 for i in range(len(s)+1)]
        res=0
        # print(arr)
        for i in arr:
            for j in range(i,0,-1):
                if(ch[j]==0):
                    ch[j]=1
                    break
                else:
                    res+=1
        # print(*ch)
        return res