# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, head)
        curr = head
        num_set = set(nums)
        while curr.next:
            if curr.next.val in num_set:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head.next
