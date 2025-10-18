# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.isMirror(root.left, root.right)
    
    
    def isMirror(self, root1, root2):
        
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
        
        if root1.val == root2.val:
            return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
        
        return False
        
        