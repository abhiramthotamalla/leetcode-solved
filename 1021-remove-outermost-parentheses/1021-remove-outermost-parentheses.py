class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st=[]
        res=""
        for c in s:
            if c=="(":
                if len(st)==0:
                    st.append("(0")
                else:
                    st.append("(")
                    res+="("
            else:
                if len(st[-1])==1:
                    res+=")"
                st.pop()
        return res