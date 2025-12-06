# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        vals = deque([])
        curr = head.next
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        i = 0
        curr = head.next
        while vals:
            if i % 2 == 1:
                new_val = vals.popleft()
                curr.val = new_val
                curr = curr.next
                i += 1
            else:
                new_val = vals.pop()
                curr.val = new_val
                curr = curr.next
                i += 1