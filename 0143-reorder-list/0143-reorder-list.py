# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, head) -> None:

        curr = head
        if not curr:
            return curr
        
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        """
            Do not return anything, modify head in-place instead.
        """
        dummy = ListNode(0,head)
        slow ,fast= dummy, dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        rev = slow.next
        slow.next = None
        rev = self.reverse(rev)

        del slow, fast

        temp = dummy.next

        while temp and rev:
            nxt = rev.next
            tmpnxt = temp.next
            temp.next = rev
            rev.next = tmpnxt
            rev = nxt
            temp = tmpnxt
        
        return dummy.next

            



        