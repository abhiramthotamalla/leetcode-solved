class Solution:
    def bagOfTokensScore(self, token: List[int], power: int) -> int:
        token.sort()
        score=0
        res=0
        i,j=0,len(token)-1
        while(i<=j):
            if token[i]<=power:
                power-=token[i]
                res+=1
                score=max(score,res)
                i+=1
            elif res>0:
                res-=1
                power+=token[j]
                j-=1
            else:
                break
        return score