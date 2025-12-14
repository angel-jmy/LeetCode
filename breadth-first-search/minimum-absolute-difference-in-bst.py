# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        nodes = []
        def preorder(node):
            if not node:
                return

            heapq.heappush(nodes, node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        node0 = heapq.heappop(nodes)
        print(node0)
        diff = 10 ** 5
        while nodes:
            node1 = heapq.heappop(nodes)
            print(node1)
            diff = min(diff, node1 - node0)
            node0 = node1

        return diff



