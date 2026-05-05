# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        stack = [root]
        res = TreeNode(1000)
        while stack:

            node = stack.pop()
            if not node:
                break
            if (node.val > p.val and node.val < q.val) or (node.val > q.val and node.val < p.val): 
                return node
            elif node.val > p.val and node.val > q.val:
                if res.val > node.val:
                    res = node
                stack.append(node.left)
            elif node.val == p.val:
                return p
            elif node.val == q.val:
                return q 
            else:
                if res.val< node.val:
                    res = node
                stack.append(node.right)

        return res
        