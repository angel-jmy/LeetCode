class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 0
        N = len(nums)
        max_lth = 0

        while r < N:
            if nums[r] == 1:
                max_lth = max(max_lth, r - l + 1)
                r += 1
            else:
                l = r + 1
                r = l

        return max_lth