class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        for x in range(1, n + 1):
            # Find how many numbers >= x
            # The first index where nums[i] >= x
            i = 0
            while i < n and nums[i] < x:
                i += 1
            if n - i == x:
                return x

        return -1