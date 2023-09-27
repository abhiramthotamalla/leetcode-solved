class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res=["1"]
        one,zero=-1,0
        for i in s:
            if i=="1":
                one+=1
            else:
                zero+=1
        for i in range(zero):
            res.append("0")
        for i in range(one):
            res.append("1")
        res=res[::-1]
        return "".join(res)