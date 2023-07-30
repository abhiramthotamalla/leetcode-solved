import heapq
class Solution:
    def minSum(self, arr, n):
        
        heapq.heapify(arr)
        num1=0
        num2=0
        i=1
        while(arr):
            if i%2==0:
                num1=num1*10+heapq.heappop(arr)
            else:
                num2=num2*10+heapq.heappop(arr)
            i+=1
        return num1+num2
        
    


#{ 
 # Driver Code Starts
import heapq as hq

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minSum(arr,n))

# } Driver Code Ends