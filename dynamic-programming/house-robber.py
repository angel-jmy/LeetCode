class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # N = len(nums)
        # if N == 1:
        #     return nums[0]
        # if N == 2:
        #     return max(nums[0], nums[1])

        # dp = [0] * N
        # dp[0] = nums[0]
        # dp[1] = max(dp[0], nums[1])

        # for i in range(2, N):
        #     dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        # return dp[N - 1]


        N = len(nums)
        dp = [0] * (N + 1)
        dp[1] = nums[0]

        for i in range(2, N + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
            

        return dp[N]
