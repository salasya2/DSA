# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:



        def dfs(p,q):
            res = True
            if p == None and q == None:
                return True
            if (p == None and q!=None) or (q==None and p!=None):
                
                return False
            if p.val != q.val:
                return False
            if (p.right == None and q.right!=None) or (q.right == None and p.right !=None):
                return False
            if (p.left == None and q.left!=None) or (q.left == None and p.left!=None):
                return False
            res = res and dfs(p.right,q.right)
            res = res and dfs(p.left,q.left)

            return res
        return dfs(p,q)
        