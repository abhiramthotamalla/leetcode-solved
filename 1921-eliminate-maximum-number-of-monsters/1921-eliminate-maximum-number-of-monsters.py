class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        sp=[]
        res=0
        for d,t in zip(dist,speed):
            speed=math.ceil(d/t)
            sp.append(speed)
        sp.sort()
        for i in range(len(sp)):
            if i>=sp[i]:
                return res
            res+=1
        return res