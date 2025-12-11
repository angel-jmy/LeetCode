# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # boolean = True
        def inorder(node):
            # nonlocal boolean
            if not node:
                return True
            if node.val == 0:
                return False
            if node.val == 1:
                return True
            if node.val == 2:
                return inorder(node.left) or inorder(node.right)
            else:
                return inorder(node.left) and inorder(node.right)

        return inorder(root)
