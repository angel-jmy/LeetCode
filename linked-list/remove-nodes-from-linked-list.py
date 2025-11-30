# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy

        while curr.next:
            if curr.next.val < self.findLarge(curr.next):
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next


    def findLarge(self, node):
        if not node.next:
            return 0
        
        return max(node.next.val, self.findLarge(node.next))