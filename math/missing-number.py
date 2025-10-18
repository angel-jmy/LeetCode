class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = 0
        max_num = len(nums)

        for num in range(min_num, max_num + 1):
            if num not in nums:
                return num