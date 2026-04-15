# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp1 = l1
        temp2 = l2
        
        dummy = ListNode()
        carry = 0
        temp = dummy

        while temp1 and temp2:

            temp.next = ListNode(0)
            val = temp1.val + temp2.val + carry

            temp.next.val = val % 10 
            carry = val//10     
            temp1 = temp1.next
            temp2 = temp2.next
            temp = temp.next

        
        
        while temp1:
            val = temp1.val + carry
            temp.next = ListNode(val%10)
            temp = temp.next
            temp1 = temp1.next
            carry = val // 10
        while temp2:
            val = temp2.val + carry
            temp.next= ListNode(val % 10)
            temp = temp.next
            temp2 = temp2.next
            carry = val // 10
        
        if carry > 0:
            temp.next = ListNode(carry)
              
        

        return dummy.next