class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # nums = sorted(nums, reverse = True)
        curr_sum = 0
        N = len(nums)
        min_len = N + 1
        l, r = 0, 0
        # length = 0

        for r in range(N):
            curr_sum += nums[r]
            # length += 1
            while curr_sum >= target:
                min_len = min(min_len, r - l + 1)
                curr_sum -= nums[l]
                l += 1               
            # r += 1

        return min_len if min_len <= N else 0
