class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        if left == right:
            return nums[left]

        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            return self.findMin(nums[mid + 1 :])

        return self.findMin(nums[:mid + 1])