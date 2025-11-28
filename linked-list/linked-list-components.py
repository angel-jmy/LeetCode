# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_set = set(nums)
        res_set = set()
        counter = 0
        prev = -1
        while head:
            val = head.val
            if val in num_set:
                if prev in res_set:
                    pass
                else:
                    counter += 1
                res_set.add(val)

            prev = val
            head = head.next

        return counter