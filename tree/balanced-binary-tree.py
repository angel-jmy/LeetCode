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

        if not root.left and not root.right:
            return True

        if not root.right:
            return self.treeHeight(root.left) <= 1

        if not root.left:
            return self.treeHeight(root.right) <= 1
        
        return abs(self.treeHeight(root.left) - self.treeHeight(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)



    def treeHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1

        return 1 + max(self.treeHeight(root.left), self.treeHeight(root.right))