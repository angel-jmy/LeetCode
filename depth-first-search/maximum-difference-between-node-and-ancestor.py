# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        diff_ = 0
        def postorder(node) -> tuple: # (max, min)
            nonlocal diff_

            if not node:
                return -1, 10 ** 5 + 1

            if not node.left and not node.right:
                return node.val, node.val

            if not node.right:
                max_l, min_l = postorder(node.left)
                diff_ = max(abs(node.val - max_l), abs(node.val - min_l), diff_)
                return max(node.val, max_l), min(node.val, min_l)

            if not node.left:
                max_r, min_r = postorder(node.right)
                diff_ = max(abs(node.val - max_r), abs(node.val - min_r), diff_)
                return max(node.val, max_r), min(node.val, min_r)


            max_l, min_l = postorder(node.left)
            max_r, min_r = postorder(node.right)

            max_0 = max(max_l, max_r)
            min_0 = min(min_l, min_r)

            diff_ = max(abs(node.val - max_0), abs(node.val - min_0), diff_) 
            # print(diff_)
            return max(node.val, max_0), min(node.val, min_0)

        postorder(root)

        return diff_
