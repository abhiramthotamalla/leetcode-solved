class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res=''
        for i in range(len(word)):
            res+=word[i]
            if word[i]==ch:
                res=res[::-1]
                break
            
        while(i+1<len(word)):
            res+=word[i+1]
            i+=1
        return res