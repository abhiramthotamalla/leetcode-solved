# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        l=[]
        q=collections.deque()
        q.append(root)
        while(q):
            cur=[]
            for p in range(len(q)):
                n=q.popleft()
                if n:
                    cur.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if cur:
                l=cur
        return l[0]