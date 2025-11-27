# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_dist = float('inf')
        # max_dist = 0
        curr = head
        pos = 0
        prev = 0
        first = 0
        while curr.next and curr.next.next:
            if curr.next.val > curr.val and curr.next.val > curr.next.next.val:
                if prev:
                    min_dist = min(pos + 1 - prev, min_dist)
                    max_dist = pos + 1 - first
                else:
                    first = pos + 1
                
                prev = pos + 1
            elif curr.next.val < curr.val and curr.next.val < curr.next.next.val:
                if prev:
                    min_dist = min(pos + 1 - prev, min_dist)
                    max_dist = pos + 1 - first
                else:
                    first = pos + 1
                    
                prev = pos + 1

            pos += 1
            curr = curr.next

        return [min_dist, max_dist] if min_dist != float('inf') else [-1, -1]