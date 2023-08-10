class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        contain=0
        maxl,maxr=height[l],height[r]
        while(l<r):
            if(maxl<maxr):
                l+=1
                maxl=max(height[l],maxl)
                contain+=maxl-height[l]
            else:
                r-=1
                maxr=max(maxr,height[r])
                contain+=maxr-height[r]
        return contain