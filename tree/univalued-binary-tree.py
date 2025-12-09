# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value = root.val

        def preorder(node):
            nonlocal value
            if not node:
                return True

            return node.val == value and preorder(node.left) and preorder(node.right)

        return preorder(root)

        
