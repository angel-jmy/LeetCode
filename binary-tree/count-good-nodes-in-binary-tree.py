# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        def preorder(node, pre_max):
            nonlocal counter
            if not node:
                return

            if node.val >= pre_max:
                counter += 1
                preorder(node.left, node.val)
                preorder(node.right, node.val)

            else:
                preorder(node.left, pre_max)
                preorder(node.right, pre_max)

        preorder(root, -10 ** 4 - 1)

        return counter