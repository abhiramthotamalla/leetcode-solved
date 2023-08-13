#User function Template for python3
class Solution:
    def commonSubseq (ob, S1, S2):
        # code here 
        flag=0
        for i in S1:
            for j in S2:
                if(i==j):
                    return 1

        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S1, S2 = input().split()
        
        ob = Solution()
        print(ob.commonSubseq(S1, S2))
# } Driver Code Ends