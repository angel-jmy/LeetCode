# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        counts = 0
        def postorder(node) -> tuple: # (avg, #nodes)
            nonlocal counts

            if not node:
                return 0, 0

            avg_left, cnt_left = postorder(node.left)
            avg_right, cnt_right = postorder(node.right)

            cnt_new = cnt_left + cnt_right + 1
            avg_new = (avg_left * cnt_left + avg_right * cnt_right + node.val) / cnt_new

            if node.val == int(avg_new):
                # print(node.val)
                counts += 1

            return avg_new, cnt_new

        postorder(root)

        return counts