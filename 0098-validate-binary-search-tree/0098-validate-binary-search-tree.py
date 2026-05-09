# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        q = collections.deque()

        q.append([root, -float("inf"),float("inf")])

        while q:

            qLen = len(q)

            for i in range(qLen):

                node, minLimit, maxLimit= q.popleft()

                if node:

                    if node.val <= minLimit or node.val >= maxLimit:
                        return False
                    
                    q.append([node.left,minLimit, min(maxLimit, node.val)])
                    q.append([node.right, max(minLimit,node.val),maxLimit])
        return True
        