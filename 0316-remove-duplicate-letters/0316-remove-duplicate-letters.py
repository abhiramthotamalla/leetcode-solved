class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen=[False for i in range(26)]
        occure=[0 for i in range(26)]
        stack=[]
        for c in s:
            occure[ord(c)-ord("a")]+=1

        for i in range(len(s)):
            # If not in the stack
            if seen[ord(s[i])-ord("a")]:
                occure[ord(s[i])-ord("a")]-=1
                continue

            while(stack and ord(stack[-1])>ord(s[i])) and occure[ord(stack[-1])-ord("a")]>0:
                seen[ord(stack[-1])-ord("a")]=False
                stack.pop()
            stack.append(s[i])
            seen[ord(s[i])-ord("a")]=True
            occure[ord(s[i])-ord("a")]-=1
        ans=[]
        while(stack):
            ans.append(stack.pop())
        ans.reverse()
        ans="".join(ans)
        return ans