#User function Template for python3

class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        #Your code here
        x=n
        l=arr
        sum=0
        d=dict()
        res=0
        d[0]=1
        for i in range(x):
            if(l[i]==0):
                sum-=1
            else:
                sum+=1
            if sum in d:
                res+=d[sum]
                d[sum]+=1
            else:
                d[sum]=1
        return (res)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        obj = Solution()
        print(obj.countSubarrWithEqualZeroAndOne(arr, n))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends