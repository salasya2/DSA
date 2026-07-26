# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = 0
        if len(inorder) ==0 or len(preorder) == 0:
            return None
        for i in range(len(preorder)):
            if inorder[i] == preorder[0]:
                idx = i
                break
        
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1: 1 + idx],inorder[:idx])
        root.right= self.buildTree(preorder[ 1 + idx :], inorder[idx + 1:])
        return root