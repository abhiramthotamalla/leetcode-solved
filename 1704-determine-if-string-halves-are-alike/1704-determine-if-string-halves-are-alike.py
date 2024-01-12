class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1=s[:(len(s)+1)//2]
        s2=s[(len(s)+1)//2:]
        print(s1,s2)
        c1,c2=0,0
        v=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for c in s1:
            if c in v:
                c1+=1
        for c in s2:
            if c in v:
                c2+=1
        return c1==c2