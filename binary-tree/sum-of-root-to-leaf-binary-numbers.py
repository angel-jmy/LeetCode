# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        sum_ = 0

        def preorder(node, curr):
            nonlocal sum_
            if not node:
                return
            if not node.left and not node.right:
                curr = curr << 1 | node.val
                sum_ += curr
                return

            preorder(node.left, curr << 1 | node.val)
            preorder(node.right, curr << 1 | node.val)

        preorder(root, 0)

        return sum_