# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self,node):
        self.node = node
    def __lt__(self,other):
        return self.node.val < other.node.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        k = len(lists)

        min_heap = []

        for i in range(k):
            if lists[i]:
                heapq.heappush(min_heap,NodeWrapper(lists[i]))
        
        dummy = ListNode(0)
        curr = dummy
        while min_heap:
            node_wrapper = heapq.heappop(min_heap)
            node = node_wrapper.node
            curr.next = node
            if node.next:
                heapq.heappush(min_heap,NodeWrapper(node.next))
            curr = curr.next
        return dummy.next
        