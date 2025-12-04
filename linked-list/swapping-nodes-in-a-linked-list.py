# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next:
            length += 1
            if length == k:
                val1 = curr.next.val
                # slow = curr
            curr = curr.next

        tgt = length - k
        curr = dummy
        i = 0
        while curr.next:
            if i < tgt:
                i += 1
                curr = curr.next
            elif i == tgt:
                # fast = curr
                val2 = curr.next.val
                # fast.next = ListNode(val1, fast.next.next)
                break

        res = ListNode(0)
        pointer = res
        curr = dummy
        i = 0
        while curr.next:
            if i == tgt:
                pointer.next = ListNode(val1)
            elif i == k - 1:
                pointer.next = ListNode(val2)
            else:
                pointer.next = ListNode(curr.next.val)

            curr = curr.next
            pointer = pointer.next
            i += 1

        return res.next