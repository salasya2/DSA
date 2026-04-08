# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    
    def reverseList(self,head:Optional[ListNode]) -> ListNode:
        if head is None:
            return head
        
        prev = None
        curr = head
        nex = None

        while curr:

            nex = curr.next
            curr.next = prev
            prev  = curr
            curr = nex


        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        mid = self.reverseList(slow.next)
        
        slow.next = None

        slow = fast = head
        
        while slow and mid:
            fast = slow.next
            temp = mid.next

            slow.next = mid
            mid.next = fast
            
            slow = fast
            mid = temp



  