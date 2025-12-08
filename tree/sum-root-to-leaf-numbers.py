# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum_ = 0

        def preorder(node, curr):
            nonlocal sum_

            if not node:
                # sum_ += curr
                return
            
            if not node.left and not node.right:
                curr = 10 * curr + node.val
                sum_ += curr
                return

            preorder(node.left, 10 * curr + node.val)
            preorder(node.right, 10 * curr + node.val)

        preorder(root, 0)

        return sum_