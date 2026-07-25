# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        '''
            Given subroot and root -> return true if subtree of root
        '''
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False 
        if self.helper(root,subRoot):
            return True
        if self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot):
            return True

        return False

    def helper(self,root,subRoot):

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        if root.val == subRoot.val  and self.helper(root.left,subRoot.left) and self.helper(root.right,subRoot.right):
            return True
        
        return False
