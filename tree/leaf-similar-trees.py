# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        vals1 = self.getLeaves(root1)
        vals2 = self.getLeaves(root2)
        # print(vals1)
        # print(vals2)
        return vals1 == vals2

    def getLeaves(self, root):
        res = []
        def preorder(node):
            if not node:
                return
            if not node.left and not node.right:
                res.append(node.val)
                return

            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return res