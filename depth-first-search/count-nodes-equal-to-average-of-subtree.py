# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        counts = 0
        def postorder(node) -> tuple: # (total, #nodes)
            nonlocal counts

            if not node:
                return 0, 0

            tot_left, cnt_left = postorder(node.left)
            tot_right, cnt_right = postorder(node.right)

            cnt_new = cnt_left + cnt_right + 1
            tot_new = tot_left + tot_right + node.val

            if node.val == tot_new // cnt_new:
                # print(node.val)
                counts += 1

            return tot_new, cnt_new

        postorder(root)

        return counts