# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        '''
        - p != q
        - a node can be parent of itself
        - node is a lowest common ancestor of p, q if  p and q are on opposite branches of the node.
        - else it has to be either p or q. Whichever comes first 
        
        '''

        temp  =root

        while temp:

            if p.val < temp.val < q.val or q.val < temp.val < p.val:
                return temp
            
            if p.val == temp.val or q.val == temp.val:
                return temp
            
            if p.val < temp.val:
                temp = temp.left
            else:
                temp = temp.right
        
        return root

        #O(n)
        # O(n)

        