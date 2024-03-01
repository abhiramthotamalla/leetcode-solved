class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s=list(s)
        s.sort()
        i=0
        while(i<len(s)):
            if s[i]=="1":
                break
            i+=1
        s[i],s[0]=s[0],s[i]
        s=s[::-1]
        return "".join(s)