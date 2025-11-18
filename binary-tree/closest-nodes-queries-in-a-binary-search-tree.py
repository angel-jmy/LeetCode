# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        nums = self.flatten(root)
        print(nums)
        N = len(nums)
        res = []
        for q in queries:
            min_i = bisect_right(nums, q)
            if min_i >= N:
                if nums[min_i - 1] <= q:
                    min_ = nums[min_i - 1]
                else:
                    min_ = -1
            elif min_i > 0 and nums[min_i - 1] <= q:
                min_ = nums[min_i - 1]
            elif min_i == 0 and nums[min_i] > q:
                min_ = -1
            else:
                min_ = nums[min_i]
            max_i = bisect_left(nums, q)
            if max_i >= N:
                max_ = -1
            else:
                max_ = nums[max_i]
            res.append([min_, max_])
        return res
        
    
    def flatten(self, root) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        if not root.right:
            return self.flatten(root.left) + [root.val]

        if not root.left:
            return [root.val] + self.flatten(root.right)

        return self.flatten(root.left) + [root.val] + self.flatten(root.right)
