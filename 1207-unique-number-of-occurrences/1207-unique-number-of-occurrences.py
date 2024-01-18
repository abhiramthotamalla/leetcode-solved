class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d=dict()
        for i in arr:
            d[i]=d.get(i,0)+1
        res=[[] for i in range(len(arr)+1)]
        for i in d:
            if res[d[i]]==[]:
                res[d[i]].append(i)
            else:
                return False
        # print(res)
        return True