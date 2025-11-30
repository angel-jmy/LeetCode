# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            # If this node starts a duplicate run
            if curr.next and curr.val == curr.next.val:
                dup_val = curr.val
                # Skip every node with this value
                while curr and curr.val == dup_val:
                    curr = curr.next
                # Link prev to the first node *after* the duplicates
                prev.next = curr
            else:
                # This value is unique: keep it and move prev
                prev = curr
                curr = curr.next

        return dummy.next