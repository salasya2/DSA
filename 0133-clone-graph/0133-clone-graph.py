"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return node
        original2ClonedMap = {}

        stack = []
        stack.append(node)
        

        def dfs(node):
            if (node is None) or (node in original2ClonedMap.keys()):
                return
                
            original2ClonedMap[node] = Node(node.val)
            if node.neighbors:
                for neigh in node.neighbors:
                    dfs(neigh)
            
            
            for neigh in node.neighbors:
                original2ClonedMap[node].neighbors.append(original2ClonedMap[neigh])
            print(original2ClonedMap[node].val, original2ClonedMap[node].neighbors)

        dfs(node)
        return original2ClonedMap[node]


        