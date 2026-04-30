# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxheight(self,root: Optional[TreeNode]) ->int:

        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1
        
        return 1+max(self.maxheight(root.right),self.maxheight(root.left))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0
        
        return max((self.maxheight(root.right)+self.maxheight(root.left)), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))