# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = head
        while curr and curr.next:
            new_val = gcd(curr.val, curr.next.val)
            temp = ListNode(new_val, curr.next)
            curr.next = temp
            curr = curr.next.next

        return head