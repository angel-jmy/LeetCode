# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        length = 0

        def dfs1(node, left, d):
            nonlocal length
            if not node:
                return
            if left: 
                if node.right:
                    length = max(length, d + 1)
                    dfs1(node.right, False, d + 1)
                else:
                    dfs1(node.left, True, 0)
                    dfs1(node.left, False, 0)

            else:
                if node.left:
                    length = max(length, d + 1)
                    dfs1(node.left, True, d + 1)
                else:
                    dfs1(node.right, True, 0)
                    dfs1(node.right, False, 0)


        def dfs2(node, left, d):
            nonlocal length
            if not node:
                return
            if left: 
                if node.left:
                    length = max(length, d + 1)
                    dfs2(node.left, False, d + 1)
                else:
                    dfs2(node.right, True, 0)
                    dfs2(node.right, False, 0)

            else:
                if node.right:
                    length = max(length, d + 1)
                    dfs2(node.right, True, d + 1)
                else:
                    dfs2(node.left, True, 0)
                    dfs2(node.left, False, 0)


        dfs1(root, True, 0)
        dfs1(root, False, 0)

        dfs2(root, True, 0)
        dfs2(root, False, 0)

        return length

    