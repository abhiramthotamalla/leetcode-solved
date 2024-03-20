class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        radius=0
        houses.sort()
        heaters.append(float("inf"))
        heaters.append(float("-inf"))
        heaters.sort()
        i=1
        for house in houses:
            while(heaters[i]<house):
                i+=1
            mini=min((heaters[i]-house),(house-heaters[i-1]))
            radius=max(mini,radius)
        return radius