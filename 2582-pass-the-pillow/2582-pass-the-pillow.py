class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i=1
        inc=1
        while(time):
            if i==n:
                inc=0
            if i==1:
                inc=1
            if inc:
                i+=1
            else:
                i-=1
            time-=1
        return i
                