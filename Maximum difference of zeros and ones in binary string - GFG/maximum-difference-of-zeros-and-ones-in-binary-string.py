#User function Template for python3
class Solution:
	def maxSubstring(self, S):
		maxi=-int(1e09)
		s=0
		for i in S:
		    if(i=="0"):
		        x=1
		    else:
		        x=-1
		    s+=x
		    if(s>maxi):
		        maxi=s
		    if(s<0):
		        s=0
	    return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.maxSubstring(s)
		print(answer)

# } Driver Code Ends