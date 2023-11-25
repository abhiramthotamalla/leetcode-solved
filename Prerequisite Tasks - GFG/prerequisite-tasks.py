#User function Template for python3
from collections import deque
class Solution:
    def isPossible(self,N,P,prerequisites):
        #code here
        adj=[[] for i in range(N)]
        for l in prerequisites:
            adj[l[0]].append(l[1])
        #making the indegree array
        inde=[0 for i in range(N)]
        for l in range(N):
            for k in adj[l]:
                inde[k]+=1
        #creating the queue
        q=deque()
        for i in range(N):
            if inde[i]==0:
                q.append(i)
        c=0
        while(q):
            node=q.popleft()
            c+=1
            for k in adj[node]:
                inde[k]-=1
                if inde[k]==0:
                    q.append(k)
        if c==N:
            return True
        return False
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,P,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends