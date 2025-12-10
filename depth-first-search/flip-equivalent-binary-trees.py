# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        if root1 and not root2:
            return False

        if root1.val != root2.val:
            return False

        dq1, dq2 = deque([root1]), deque([root2])


        while dq1 and dq2:
            size1, size2 = len(dq1), len(dq2)
            # if size1 != size2:
            #     return False

            for _ in range(size1):
                node1, node2 = dq1.popleft(), dq2.popleft()
                # if node1.val != node2.val:
                #     return False
                
                same = self.equal(node1.left, node2.left) and self.equal(node1.right, node2.right)
                mirror = self.equal(node1.left, node2.right) and self.equal(node1.right, node2.left)
                if not same and not mirror:
                    return False

                if same:
                    if node1.left:
                        dq1.append(node1.left)
                    if node1.right:
                        dq1.append(node1.right)
                    if node2.left:
                        dq2.append(node2.left)
                    if node2.right:
                        dq2.append(node2.right)

                else:
                    if node1.left:
                        dq1.append(node1.left)
                    if node1.right:
                        dq1.append(node1.right)
                    if node2.right:
                        dq2.append(node2.right)
                    if node2.left:
                        dq2.append(node2.left)

        return not dq1 and not dq2


    def equal(self, n1, n2):
        if n1 is None and n2 is None:
            return True
        if n1 is None or n2 is None:
            return False
        return n1.val == n2.val
