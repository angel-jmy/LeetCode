# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        d = 1
        stack = deque([root])
        while stack:
            level_size = len(stack)
            if d < depth - 1:
                for i in range(level_size):
                    node = stack.popleft()
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)

                d += 1
            
            elif d == depth - 1:
                for i in range(level_size):
                    node = stack.popleft()
                    if node.left:
                        node.left = TreeNode(val, node.left)
                    if node.right:
                        node.right = TreeNode(val, None, node.right)

                break

        print(d)

        return root
