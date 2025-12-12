# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        counts = []

        def postorder(node) -> tuple: # (Number, Bool) --> whether itself is perfect
            if not node:
                return 0, False

            if not node.left and not node.right:
                heapq.heappush(counts, -1)
                return 1, True

            if not node.right:
                num, boo = postorder(node.left)
                return num, False

            if not node.left:
                num, boo = postorder(node.right)
                return num, False

            num1, boo1 = postorder(node.left)
            num2, boo2 = postorder(node.right)

            if boo1 and boo2 and num1 == num2:
                num = num1 + num2 + 1
                heapq.heappush(counts, -num)
                boo = True
                return num, boo

            return num1 + num2, False

        postorder(root)

        N = len(counts)
        if k > N:
            return -1

        # print(counts)
        for _ in range(k - 1):
            heapq.heappop(counts)

        return -heapq.heappop(counts)