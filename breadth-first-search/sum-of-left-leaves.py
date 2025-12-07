# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum_ = 0

        def preorder(node, left):
            nonlocal sum_
            if not node.left and not node.right:
                if left:
                    sum_ += node.val
                    return
                return

            preorder(node.left, True)
            preorder(node.right, False)


        preorder(root, False)

        return sum_