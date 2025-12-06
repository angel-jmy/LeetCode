# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        pointer = res
        if not head or not head.next:
            return head
        
        curr = head
        while curr:
            pointer.next = ListNode(curr.val)
            pointer = pointer.next
            if curr.next:
                curr = curr.next.next
            else:
                break

        curr = head.next
        
        while curr:
            pointer.next = ListNode(curr.val)
            pointer = pointer.next
            if curr.next:
                curr = curr.next.next
            else:
                break

        return res.next