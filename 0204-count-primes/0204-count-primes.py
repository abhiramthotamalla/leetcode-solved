class Solution:
    def countPrimes(self, n: int) -> int:
        if(n==0):
            return 0
        l=[1 for i in range(n+1)]
        if(n>=1):
            l[0],l[1]=0,0
        for i in range(2,n+1):
            if(l[i]==1):
                for j in range(i*2,n+1,i):
                    l[j]=0
        for i in range(1,n+1):
            l[i]=l[i-1]+l[i]
        return l[n-1]