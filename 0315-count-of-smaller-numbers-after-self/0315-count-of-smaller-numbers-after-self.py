from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s=SortedList()
        output=[]
        for p in nums[::-1]:
            ans=SortedList.bisect_left(s,p)
            output.append(ans)
            s.add(p)
        return reversed(output)