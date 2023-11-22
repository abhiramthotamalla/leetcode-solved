class Solution:
	def isBipartite(self, V, adj):
		#code here
		def dfs(node,col):
		    vis[node]=col
		    for it in adj[node]:
		        if vis[it]==-1:
                    if dfs(it,1-col)==False:
        		            return False
                elif vis[it]==col:
                    return False
            return True
            
        vis=[-1 for i in range(V)]
        for i in range(V):
            if vis[i]==-1:
                if dfs(i,0)==False:
                    return False
        return True
                


#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends