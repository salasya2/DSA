# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSametree(self,p,q):
        
        stack = [[p,q]]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            if not (node1 and node2) or (not node2 and node1) or (node2.val!=node1.val):
                return False
            
            stack.append([node1.left,node2.left])
            stack.append([node1.right,node2.right])
        return True
            
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNodse]) -> bool:

        if not root and not subroot :
            return True

        stack = [root]

        while stack:
            node  = stack.pop()
            
            if node:
                if node.val == subRoot.val:
                    flag = self.isSametree(node,subRoot)
                    if flag:
                        return flag
                stack.append(node.left)
                stack.append(node.right)
        
        return False

            



        