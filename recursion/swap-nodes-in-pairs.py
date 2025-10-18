# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        curr = head          # keep pointer to original head
        head = head.next     # new head is the second node
        prev = None          # tail of the last swapped pair

        while curr and curr.next:
            temp = curr.next     # second in the pair
            tail = temp.next     # head of the remaining list

            # swap the pair (temp <-> curr)
            temp.next = curr
            curr.next = tail

            # connect previous pair to current swapped pair
            if prev:
                prev.next = temp

            # advance pointers
            prev = curr
            curr = tail

        return head