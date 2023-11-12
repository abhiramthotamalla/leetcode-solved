class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]:
            return "0"
        resl=len(num1)+len(num2)
        res=[0]*resl
        num1,num2=num1[::-1],num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i])*int(num2[j])
                res[i+j]+=digit
                res[i+j+1]+=res[i+j]//10
                res[i+j]=res[i+j]%10
        i=-1
        while(res[i]==0):
            res.pop()
        res=map(str,res[::-1])
        return "".join(res)