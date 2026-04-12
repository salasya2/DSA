"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        new_head = Node(0)
        if head is None:
            return head

        temp = new_head
        curr = head
        d = collections.defaultdict(lambda : Node(0))
        d[None] = None

        while curr:

            d[curr].val = curr.val
            d[curr].next = d[curr.next]
            d[curr].random = d[curr.random]
            curr = curr.next      

        return d[head]
            