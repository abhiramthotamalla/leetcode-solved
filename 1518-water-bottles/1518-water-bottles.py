class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res=numBottles
        while(numBottles//numExchange):
            dum=numBottles//numExchange
            res+=dum
            numBottles=dum+(numBottles%numExchange)
        return res