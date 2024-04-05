class Solution:
    def makeGood(self, s: str) -> str:
        st=[]
        i=0
        while(i<len(s)):
            st.append(s[i])
            i+=1
            while(len(st)>=2 and ((st[-1]==st[-2].upper() and st[-1]!=st[-2]) or (st[-1]==st[-2].lower() and st[-1]!=st[-2]))):
                st.pop()
                st.pop()
            # i+=1
        return "".join(st)