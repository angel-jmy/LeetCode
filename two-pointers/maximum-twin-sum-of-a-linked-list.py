# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        mid = n // 2
        i = 1
        first = head
        while first.next:
            if i < mid:
                i += 1
                first = first.next
            elif i == mid:
                second = first.next
                break

        second = self.reverseList(second)
        first = head
        max_ = 0
        for i in range(mid):
            val1 = first.val
            val2 = second.val
            max_ = max(max_, val1 + val2)
            first = first.next
            second = second.next

        return max_



    def reverseList(self, node):
        if not node:
            return

        curr = node.next
        res = ListNode(node.val)
        while curr:
            res = ListNode(curr.val, res)
            curr = curr.next

        return res