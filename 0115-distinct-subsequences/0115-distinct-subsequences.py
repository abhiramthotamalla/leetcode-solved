class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        d=dict()
        def help(i,j):
            if(j<0):
                return 1
            if i<0:
                return 0
            if (i,j) in d:
                return d[(i,j)]
            if(s[i]==t[j]):
                take=help(i-1,j-1)
                nottake=help(i-1,j)
                d[(i,j)]=take+nottake
                return d[(i,j)]
            else:
                d[(i,j)]=help(i-1,j)
                return d[(i,j)]
        return help(len(s)-1,len(t)-1)