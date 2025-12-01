# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = ListNode(0, head.next)
        
        res = ListNode(0)
        res.next = ListNode(head.val)

        while curr.next:
            pointer = res
            while pointer.next:
                if pointer.next.val > curr.next.val:
                    pointer.next = ListNode(curr.next.val, pointer.next)
                    # curr.next = curr.next.next
                    break
                else:
                    pointer = pointer.next
            else:
                pointer.next = ListNode(curr.next.val)
            
            curr.next = curr.next.next

        return res.next