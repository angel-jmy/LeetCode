class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # cur_max, max_till_now = 0, -float('inf')
        # for c in nums:
        #     cur_max = max(c, cur_max + c)
        #     max_till_now = max(max_till_now, cur_max)
        # return max_till_now

        cur = best = nums[0]
        start = 0
        best_l = best_r = 0

        for i in range(1, len(nums)):
            if nums[i] > cur + nums[i]:
                cur = nums[i]
                start = i         # start new subarray at i
            else:
                cur += nums[i]    # extend

            if cur > best:
                best = cur
                best_l, best_r = start, i

        return best