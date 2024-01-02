class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        maxi=0
        i=0
        while(i<len(nums)-1):
            c=0
            j=i+1
            while(j<len(nums)):
                if nums[i]==nums[j]:
                    c+=1
                    j+=1
                    maxi=max(c,maxi)
                else:
                    c=0
                    break
            i=j
            
        print(maxi)
        
        res=[[] for i in range(maxi+1)]
        
        # for v in d:
        #     c=0
        #     k=d[v]
        #     while(k and c<max(k1)):
        #         if v not in res[c]:
        #             res[c].append(v)
        #             k-=1
        #         c+=1
        
        i=0
        while(i<len(nums)):
            j=i+1
            c=0
            res[c].append(nums[i])
            c+=1
            while(j<len(nums)):
                if nums[i]==nums[j]:
                    res[c].append(nums[i])
                    c+=1
                    j+=1
                else:
                    break
            i=j
                
        return res