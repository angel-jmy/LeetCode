# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        mid = length // 2 + 1
        curr = head
        i = 1
        while curr:
            if i < mid:
                i += 1
                curr = curr.next
            elif i == mid:
                return curr