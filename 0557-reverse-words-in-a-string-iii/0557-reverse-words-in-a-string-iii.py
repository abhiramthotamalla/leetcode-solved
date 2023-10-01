class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        res=[]
        for c in s:
            res.append(c[::-1])
        res=" ".join(res)
        return res