# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                # (left_len, right_len)
                return -1, -1
                # -1 so that when we add +1 → first edge becomes 0

            left_l, left_r = dfs(node.left)
            right_l, right_r = dfs(node.right)

            # If last move was LEFT, we must go RIGHT next
            left_len = left_r + 1

            # If last move was RIGHT, we must go LEFT next
            right_len = right_l + 1

            self.ans = max(self.ans, left_len, right_len)

            return left_len, right_len

        dfs(root)
        return self.ans
    