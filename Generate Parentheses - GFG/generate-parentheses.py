#User function Template for python3

class Solution:
    def AllParenthesis(self,n):
        #code here
        res=[]
        r=[]
        def check(op,cp):
            if op==cp==n:
                res.append("".join(r))
                return
            if op<n:
                r.append("(")
                check(op+1,cp)
                r.pop()
            if op>cp:
                r.append(")")
                check(op,cp+1)
                r.pop()
        check(0,0)
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends