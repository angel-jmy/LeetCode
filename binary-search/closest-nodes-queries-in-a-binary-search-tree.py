# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        res = []
        for q in queries:
            min_ = self.find_min(root, q)
            max_ = self.find_max(root, q)
            res.append([min_, max_])

        return res
        
    
    def find_min(self, root, q) -> int:
        if not root:
            return -1
        if root.val == q:
            return q
        if root.val > q:
            return self.find_min(root.left, q)
        if root.val < q:
            right = self.find_min(root.right, q)
            if right == -1:
                return root.val
            return right

    def find_max(self, root, q) -> int:
        if not root:
            return -1
        if root.val == q:
            return q
        if root.val < q:
            return self.find_max(root.right, q)
        if root.val > q:
            left = self.find_max(root.left, q)
            if left == -1:
                return root.val
            return left
