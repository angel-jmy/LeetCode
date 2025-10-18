class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        dp = [0] * (high + 1)
        dp[0] = 1
        MOD = 10 ** 9 + 7
        ans = 0

        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i - one >= 0:
                dp[i] = (dp[i] + dp[i - one]) % MOD
            if low <= i <= high:
                ans = (ans + dp[i]) % MOD

        return ans