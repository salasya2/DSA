# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        Len = 0

        temp = head

        while temp:
            Len += 1
            temp = temp.next
        if n == Len:
            return head.next

        n_from_start = Len - n
        index = 0
        temp = head
        while index < n_from_start - 1 and temp:
            temp = temp.next
            index += 1
        
        nxt = temp.next
        if nxt:
            temp.next = nxt.next
        else:
            temp.next = nxt
        return head

        