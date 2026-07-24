# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ''' sorted lists
            result - one merged sorted list
             i shouldn't copy the values.

        '''

        node1 = list1
        node2 = list2
        dummy = ListNode(0)
        head = dummy
        while node1 and node2:

            if node1.val < node2.val:
                head.next = node1
                node1 = node1.next
                head = head.next
            
            else:
                head.next = node2
                node2 = node2.next
                head = head.next

        while node1:
            head.next = node1
            node1 = node1.next
            head = head.next
        
        while node2:
            head.next = node2
            node2 = node2.next
            head = head.next
        
        return dummy.next