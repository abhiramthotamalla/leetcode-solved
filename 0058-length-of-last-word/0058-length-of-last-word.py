class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split(" ")
        while(True):
            if len(l[-1])==0:
                l.pop()
            else:
                break
        return len(l[-1])