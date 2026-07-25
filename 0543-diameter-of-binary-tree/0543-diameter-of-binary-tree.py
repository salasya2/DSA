# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        if not root:
            return 0

        stack = [root]
        diameter = 0
        heights = {}


        while stack:
            node = stack [-1]

            if (not node.left  or  node.left in heights) and (not node.right or node.right in heights):
                stack.pop()

                left_height = heights.get(node.left,0)
                right_height = heights.get(node.right,0)

                diameter= max(diameter,left_height+right_height)

                heights[node] = 1 + max(left_height, right_height)
            else:

                if node.right and node.right not in heights:
                    stack.append(node.right)
                if node.left and node.left not in heights:
                    stack.append(node.left)
        return diameter

