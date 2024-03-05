class Solution:
    def minimumLength(self, s: str) -> int:
        i,j=0,len(s)-1
        while(i<j):
            if s[i]==s[j]:
                dum=s[i]
                while(i<=j and dum==s[i]):
                    i+=1
                while(i<=j and dum==s[j]):
                    j-=1
            else:
                break

        return len(s[i:j+1])