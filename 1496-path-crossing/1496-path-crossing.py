class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited=set()
        x=0
        y=0
        visited.add((0,0))
        for p in path:
            if p=="N":
                y+=1
            elif p=="S":
                y-=1
            elif p=="E":
                x-=1
            else:
                x+=1
            if (x,y) in visited:
                return True
            else:
                visited.add((x,y))
        return False