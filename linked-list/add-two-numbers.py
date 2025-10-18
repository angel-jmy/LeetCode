# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode(0)
        curr = res
        adding = 0

        while l1 and l2:
            v1, v2 = l1.val, l2.val
            _sum = v1 + v2 + adding
            num = _sum % 10
            adding = _sum // 10
            # res = ListNode(num, res)
            curr.next = ListNode(num)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            v1 = l1.val + adding
            num = v1 % 10
            adding = v1 // 10
            # res = ListNode(num, res)
            curr.next = ListNode(num)
            curr = curr.next
            l1 = l1.next

        while l2:
            v2 = l2.val + adding
            num = v2 % 10
            adding = v2 // 10
            # res = ListNode(num, res)
            curr.next = ListNode(num)
            curr = curr.next
            l2 = l2.next
        
        if adding > 0:
            curr.next = ListNode(adding)
            curr = curr.next

        return res.next