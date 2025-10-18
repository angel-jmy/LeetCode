class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(1, target + 1):
            for x in nums:
                if x <= t:
                    dp[t] += dp[t - x]
        return dp[target]
