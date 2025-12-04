# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next
        
        k = k % length
        if not k:
            return head
            
        target = length - k
        # print(target)
        i = 0
        dummy = ListNode(0, head)
        slow = fast = dummy
        while fast.next:
            if i < target:
                i += 1
                fast = fast.next
            elif i == target:
                prev = fast
                fast = fast.next
                prev.next = None
                break

        new_head = fast
        while fast.next:
            fast = fast.next

        fast.next = slow.next

        return new_head



