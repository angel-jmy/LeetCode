# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        mid = length // 2 + 1
        i = 1
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next:
            if i < mid:
                i += 1
                curr = curr.next
            elif i == mid:
                curr.next = curr.next.next
                break

        return dummy.next