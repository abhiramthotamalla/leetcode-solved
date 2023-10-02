class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        i=0
        ta,tb=0,0
        s=colors
        while i<len(s):
            As=0
            while(i<len(s) and s[i]=="A"):
                As+=1
                i+=1
            if As>2:
                ta+=(As-2)
                As=0
            if i<len(s) and s[i]=="B":
                i+=1
                
        i=0

        while i<len(s):
            Bs=0
            while(i<len(s) and s[i]=="B"):
                Bs+=1
                i+=1
            if Bs>2:
                tb+=(Bs-2)
                As=0
            if i<len(s) and s[i]=="A":
                i+=1

        return ta>tb
        