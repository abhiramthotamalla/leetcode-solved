class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        res=[]
        i=1
        while(n):
            if(n and k-i not in res):
                res.append(i)
                n-=1

            i+=1
            
        
        return sum(res)