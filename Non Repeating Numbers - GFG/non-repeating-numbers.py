#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
		xor=0
		for i in range(len(nums)):
		    xor=xor^nums[i]
		n1,n2=0,0
		rms=(xor)&~(xor-1)
		for i in range(len(nums)):
		    if(rms&nums[i]):
		        n1=n1^nums[i]
		    else:
		        n2=n2^nums[i]
		return [min(n1,n2),max(n1,n2)]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends