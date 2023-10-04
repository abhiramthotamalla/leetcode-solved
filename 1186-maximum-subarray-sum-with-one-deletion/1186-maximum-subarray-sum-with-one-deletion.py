class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        maxi=max(arr)
        if maxi<0:
            return maxi
        maxl,maxr=[0 for i in range(len(arr))],[0 for i in range(len(arr))]
        curMax,bestMax=0,0
        for i in range(len(arr)):
            a=arr[i]
            curMax=max(curMax+a,a)
            maxl[i]=curMax
        curMax,bastMax=0,0
        for i in range(len(arr)-1,-1,-1):
            a=arr[i]
            curMax=max(curMax+a,a)
            bestMax=max(curMax,bestMax)
            maxr[i]=curMax
        res=bestMax
        for i in range(1,len(arr)-1):
            res=max(res,maxl[i-1]+maxr[i+1])
        return res