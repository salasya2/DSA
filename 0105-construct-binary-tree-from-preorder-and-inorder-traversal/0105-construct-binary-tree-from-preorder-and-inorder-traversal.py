# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        root = preorder[0]
        idx = 0
        mp = {}
        for i  in range(len(inorder)):
            mp[inorder[i]] = i
        
        def dfs(l,r):
            nonlocal idx
            if l > r:
                return None


            root_val = preorder[idx]
            idx += 1
            mid = mp[root_val]
            root = TreeNode(root_val)
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)
            return root
        
        return dfs(0, len(inorder) - 1)





        