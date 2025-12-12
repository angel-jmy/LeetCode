# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
    
        total_tilt = 0

        def postorder(node: Optional[TreeNode]) -> int:
            nonlocal total_tilt
            if not node:
                return 0

            left_sum = postorder(node.left)
            right_sum = postorder(node.right)

            # tilt at this node
            total_tilt += abs(left_sum - right_sum)

            # return sum of this subtree
            return left_sum + right_sum + node.val

        postorder(root)
        return total_tilt
            