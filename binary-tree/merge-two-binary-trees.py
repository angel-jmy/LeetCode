# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        # tree = TreeNode(root1.val + root2.val)
        tree = TreeNode(0)
        
        def preorder(node1, node2, pointer, left):
            if not node1:
                if left:
                    pointer.left = node2
                else:
                    pointer.right = node2
                return

            if not node2:
                if left:
                    pointer.left = node1
                else:
                    pointer.right = node1
                return

            if left:
                pointer.left = TreeNode(node1.val + node2.val)
                preorder(node1.left, node2.left, pointer.left, True)
                preorder(node1.right, node2.right, pointer.left, False)
            else:
                pointer.right = TreeNode(node1.val + node2.val)
                preorder(node1.left, node2.left, pointer.right, True)
                preorder(node1.right, node2.right, pointer.right, False)

                
        preorder(root1, root2, tree, True)

        return tree.left