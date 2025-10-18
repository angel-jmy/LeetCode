class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findLeft():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:  # go left if nums[mid] == target
                    r = mid - 1
            return l

        def findRight():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:  # go right if nums[mid] == target
                    l = mid + 1
            return r

        left = findLeft()
        right = findRight()

        # Check if target actually exists
        if left <= right:
            return [left, right]
        else:
            return [-1, -1]