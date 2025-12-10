# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def preorder(node):
            if not node:
                return 

            if self.sameTree(node, target):
                return node

            return preorder(node.left) or preorder(node.right)

        return preorder(cloned)
        


    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
        