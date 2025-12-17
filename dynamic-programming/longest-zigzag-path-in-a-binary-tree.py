# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        length = 0

        def dfs(node, left, d):
            nonlocal length
            if not node:
                return
            if left: 
                if node.right:
                    length = max(length, d + 1)
                    dfs(node.right, False, d + 1)
                else:
                    dfs(node.left, True, 0)
                    dfs(node.left, False, 0)

            else:
                if node.left:
                    length = max(length, d + 1)
                    dfs(node.left, True, d + 1)
                else:
                    dfs(node.right, True, 0)
                    dfs(node.right, False, 0)

        dfs(root, True, 0)
        dfs(root, False, 0)

        return length

    