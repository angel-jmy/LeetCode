# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return abs(self.treeHeight(root.left) - self.treeHeight(root.right)) <= 1


    def treeHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1

        return 1 + max(self.treeHeight(root.left), self.treeHeight(root.left))