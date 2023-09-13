class Solution:
    def calPoints(self, operations: List[str]) -> int:
        op=operations
        st=[]
        for i in op:
            if(i=="+"):
                st.append(st[-1]+st[-2])
            elif(i=="D"):
                st.append(2*st[-1])
            elif(i=="C"):
                st.pop()
            else:
                d=int(i)
                st.append(d)
        return sum(st)