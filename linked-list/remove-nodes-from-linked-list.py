# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        head = self.revList(head)
        # print(revhead)

        curr = head
        max_val = curr.val
        while curr.next:
            if curr.next.val < max_val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_val = curr.val

        return self.revList(head)

    def revList(self, node):
        if not node:
            return None

        curr = ListNode(node.val, None)
        while node.next:
            curr = ListNode(node.next.val, curr)
            node = node.next

        return curr
    