# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        N = len(nums)
        midIdx = N // 2
        
        if N == 1:
            return TreeNode(nums[midIdx])
        
        if N == 2:
            return TreeNode(nums[midIdx], self.sortedArrayToBST(nums[:midIdx]))
        
        return TreeNode(nums[midIdx], self.sortedArrayToBST(nums[:midIdx]), self.sortedArrayToBST(nums[midIdx + 1:]))
        