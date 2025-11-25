# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        res = 0
        def preorder(node):
            nonlocal res
            if not node:
                return
            res += 1
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return res
