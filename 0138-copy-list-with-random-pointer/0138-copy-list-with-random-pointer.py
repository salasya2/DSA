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
        dummy = Node(0)
        curr = dummy
        temp = head
        while temp:
            if temp in mapped:
                curr.next = mapped[temp]
            else:
                curr.next = Node(temp.val)
                mapped[temp] = curr.next
            random_node = temp.random
            curr = curr.next
            curr_random = curr
            
            while random_node:
                # print(random_node.val,temp.random.val, temp.val)
                if random_node in mapped:
                   
                    curr_random.random = mapped[random_node]
                    curr_random = curr_random.random
                    break
                else:
                    curr_random.random = Node(random_node.val)
                    mapped[random_node] = curr_random.random
                    curr_random = curr_random.random
                random_node = random_node.random
            
            temp = temp.next
    
        return mapped[head]