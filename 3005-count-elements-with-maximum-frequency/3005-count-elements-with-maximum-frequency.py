class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d=dict()
        for k in nums:
            d[k]=d.get(k,0)+1
        maxi=max(d.values())
        c=0
        for k,v in d.items():
            if v==maxi:
                c+=1
        return c*maxi