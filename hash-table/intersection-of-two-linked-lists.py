# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        temp1, temp2 = headA, headB
        m, n = 0, 0
        while temp1:
            m += 1
            temp1 = temp1.next

        while temp2:
            n += 1
            temp2 = temp2.next

        temp1, temp2 = headA, headB

        while temp1 and temp2 and m and n:
            if m > n:
                temp1 = temp1.next
                m -= 1
            elif n > m:
                temp2 = temp2.next
                n -= 1
            else:
                if temp1 == temp2:
                    return temp1
                else:
                    temp1 = temp1.next
                    temp2 = temp2.next
                    m -= 1
                    n -= 1

        return None

        