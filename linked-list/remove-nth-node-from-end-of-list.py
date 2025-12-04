# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        length = 0
        while curr.next:
            length += 1
            curr = curr.next

        target = length - n + 1
        i = 1
        curr = dummy
        while curr.next:
            if i < target:
                i += 1
                curr = curr.next
            elif i == target:
                curr.next = curr.next.next
                break

        return dummy.next