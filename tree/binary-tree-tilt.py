# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
    
        tilts = self.tiltTree(root)
        # print(tilts)
        return self.sumTree(tilts)
        

    def sumTree(self, root):
        sum_ = 0
        def preorder(node):
            nonlocal sum_
            if not node:
                return 
            sum_ += node.val
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return sum_

    def tiltTree(self, root) -> Optional[TreeNode]:
        def postorder(node):
            if not node:
                return None
            if not node.left and not node.right:
                return TreeNode(0)
            if not node.right:
                left = postorder(node.left)
                sum_ = self.sumTree(node.left)
                val = abs(sum_)
                return TreeNode(val, left, None)
            if not node.left:
                right = postorder(node.right)
                sum_ = self.sumTree(node.right)
                val = abs(sum_)
                return TreeNode(val, None, right)

            left = postorder(node.left)
            right = postorder(node.right)
            sum_1 = self.sumTree(node.left)
            sum_2 = self.sumTree(node.right)
            val = abs(sum_1 - sum_2)
            return TreeNode(val, left, right)

        return postorder(root)

            