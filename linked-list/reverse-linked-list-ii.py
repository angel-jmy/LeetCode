# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        idx = 1
        dummy = ListNode(0, head)

        curr = dummy
    
        while curr.next:
            if idx < left:
                curr = curr.next
                idx += 1
            elif idx == left:
                prev = curr
                mid = ListNode(curr.next.val)
                curr = curr.next
                idx += 1
            elif left < idx <= right:
                mid = ListNode(curr.next.val, mid)
                curr = curr.next
                idx += 1
            else:
                prev.next = mid
                while mid.next:
                    mid = mid.next
                mid.next = curr.next
                break
        else:
            prev.next = mid

        return dummy.next