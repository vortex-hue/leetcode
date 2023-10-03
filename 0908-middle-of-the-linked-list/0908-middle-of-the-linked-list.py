# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        shift = head
        while shift and shift.next:
            # In each iteration, we move head one node forward and we move temp two nodes forward...
            head = head.next
            shift = shift.next.next
        # When temp reaches the last node, head will be exactly at the middle point...
        return head