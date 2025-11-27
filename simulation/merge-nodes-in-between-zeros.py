# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum_ = 0
        res = ListNode(0, None)
        curr = res
        while head:
            if head.val:
                sum_ += head.val
            elif sum_ == 0:
                pass
            else:
                curr.next = ListNode(sum_, None)
                curr = curr.next
                sum_ = 0
            
            head = head.next

        return res.next
