class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        d=[]
        for s in bank:
            d.append(s.count('1'))
        # print(d)
        res=0
        prev=d[0]
        i=1
        while(i<len(bank)):
            if d[i]==0:
                i+=1
            else:
                res+=prev*d[i]
                prev=d[i]
                i+=1
        return (res) if res else 0
