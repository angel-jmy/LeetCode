# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow, fast = head, head

        while slow != None and fast != None:
            if fast.next == None:
                return slow
            elif fast.next.next == None:
                return slow.next

            slow = slow.next
            fast = fast.next.next


