class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        sumc=customers[0][1]
        pre=customers[0][0]+customers[0][1]
        for i in range(1,len(customers)):
            pre+=customers[i][1]
            if pre<=customers[i][0]+customers[i][1]:
                pre=customers[i][0]+customers[i][1]
            # print(pre,customers[i][0])
            sumc+=pre-customers[i][0]
        # print(sumc)
        return sumc/len(customers)