# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
        origin = head
        newlist = ListNode(head.val)
        head = head.next
        
        while head:         
            newlist = ListNode(head.val, newlist)
            head = head.next
            
        while origin:
            if origin.val != newlist.val:
                return False
            origin = origin.next
            newlist = newlist.next
            
        return True
            