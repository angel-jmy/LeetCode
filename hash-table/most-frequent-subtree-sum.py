# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        counts = defaultdict(int)
        def postorder(node) -> int:
            if not node:
                return 0
            left = postorder(node.left)
            right = postorder(node.right)
            sum_ = left + node.val + right
            counts[sum_] += 1
            return sum_

        postorder(root)

        sort_counts = sorted(counts.items(), key = lambda x: -x[1])
        max_count = sort_counts[0][1]
        res = []
        for item in sort_counts:
            if item[1] == max_count:
                res.append(item[0])

        return res