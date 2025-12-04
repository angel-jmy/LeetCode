# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy

        while curr.next and curr.next.next:
            after = curr.next.next.next
            val1 = curr.next.val
            val2 = curr.next.next.val
            curr.next = ListNode(val2)
            curr.next.next = ListNode(val1, after)
            curr = curr.next.next

        return dummy.next