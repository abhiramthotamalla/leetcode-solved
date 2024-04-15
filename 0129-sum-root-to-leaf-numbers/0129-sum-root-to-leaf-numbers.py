# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=[]
        def dfs(root,arr):
            if not root.right and not root.left:
                dum=arr.copy()
                dum="".join(dum)
                res.append(int(dum))
                return
            if root.left!=None:
                arr.append(str(root.left.val))
                dfs(root.left,arr)
                arr.pop()
            if root.right!=None:
                arr.append(str(root.right.val))
                dfs(root.right,arr)
                arr.pop()
        dfs(root,[str(root.val)])
        print(res)
        return sum(res)