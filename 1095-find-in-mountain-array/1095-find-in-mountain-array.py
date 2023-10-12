# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length=mountain_arr.length()
        l,r=1,length-2
        while(l<=r):
            mid=(l+r)>>1
            left,m,right=mountain_arr.get(mid-1),mountain_arr.get(mid),mountain_arr.get(mid+1)
            if left<m<right:
                l=mid+1
            elif left>m>right:
                r=mid-1
            else:
                break
        peak=mid
        l,r=0,peak
        while l<=r:
            mid=(l+r)//2
            val=mountain_arr.get(mid)
            if val<target:
                l=mid+1
            elif val>target:
                r=mid-1
            else:
                return mid
        l,r=peak,length-1
        while l<=r:
            mid=(l+r)//2
            val=mountain_arr.get(mid)
            if val>target:
                l=mid+1
            elif val<target:
                r=mid-1
            else:
                return mid
        return -1