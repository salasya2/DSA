# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr= head
        
        t = 0

        temp = head
        while temp:
            t+=1
            temp=temp.next

        print(t)
        n = t-n
        if n == 0:
            return head.next
        while n>1:
            curr = curr.next
            n-=1
        temp = curr.next
        if temp:
            temp = temp.next
            curr.next = temp
        else:
            curr.next = None

        return head
        

