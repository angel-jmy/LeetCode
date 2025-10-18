# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
                
        else:
            return None

        res = head

        while res != slow:
            res = res.next
            slow = slow.next

        return res



        