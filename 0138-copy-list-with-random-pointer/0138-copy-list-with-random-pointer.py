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
        
        '''
         - deep copy -> n brand new node
         - next and random must  point to new nodes

        '''

        mapped = {}
        if not head:
            return head
        
        curr = head

        while curr:
            mapped[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:

            mapped[curr].next = mapped.get(curr.next)
            mapped[curr].random = mapped.get(curr.random)
            curr = curr.next
    
        return mapped[head]