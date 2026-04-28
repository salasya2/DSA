# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head):

    curr = head
    prev = None

    while curr:

        nex = curr.next
        curr.next = prev
        prev = curr
        
        curr = nex
    
    return prev

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        i = 0
        curr,temp = head,head
        end = None
        while i < k and curr:
            i+=1
            if i==1:
                start = temp
            if i==k:
                temp = curr.next
                curr.next = None
                if end is None:
                    dummy.next = reverse(start)    
                else:
                    end.next = reverse(start)
                end = start
                end.next = temp
                curr = temp
                i=0
            # print(i , curr.val)
            else:
                curr = curr.next
            
            
        return dummy.next


        