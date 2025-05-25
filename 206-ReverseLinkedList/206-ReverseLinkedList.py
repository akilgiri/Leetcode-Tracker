# Last updated: 5/25/2025, 1:08:23 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            tempNode = curr.next
            curr.next = prev
            
            # Update curr and prev for next iteration
            prev = curr
            curr = tempNode

        return prev
        