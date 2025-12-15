# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nodes = []

        diff = 10 ** 6

        def inorder(node):
            nonlocal diff
            if not node:
                return

            inorder(node.left)
            if nodes:
                diff = min(diff, node.val - nodes[-1])
            nodes.append(node.val)
            inorder(node.right)

        inorder(root)

        return diff
