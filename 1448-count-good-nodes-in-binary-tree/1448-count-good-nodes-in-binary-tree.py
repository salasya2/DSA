# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0

        stack = [[root,root.val]]

        while stack:

            node, maximum = stack.pop()

            if node:
            
                maximum = max(maximum,node.val)
                if node.val == maximum:
                    res += 1
                

                stack.append([node.right,maximum])
                stack.append([node.left,maximum])
        return res


        