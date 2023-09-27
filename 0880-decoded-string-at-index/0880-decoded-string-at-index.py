class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size=0
        for i in range(len(s)):
            if s[i].isdigit():
                size=size*int(s[i])
            else:
                size+=1
        for i in range(len(s)-1,-1,-1):
            k%=size
            if (s[i].isdigit()):
                size//=int(s[i])
                k%=size
            else:
                if k==0 or k==size:
                    return s[i]
                size-=1
        return ""