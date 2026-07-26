# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        h = 0
        ans = 0
        def inorder(node):
            nonlocal ans,k,h
            if not node:
                return
            inorder(node.left)
            
            h += 1
            if k == h:
                ans = node.val
                return
            inorder(node.right)

        inorder(root)
        return ans

        
