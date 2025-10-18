# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        
        newlist = ListNode(head.val)
        head = head.next
        
        while head:         
            newlist = ListNode(head.val, newlist)
            head = head.next
            
        
        return newlist