class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [amount + 1] * amount

        for m in range(1, amount + 1):
            for c in coins:
                if c <= m:
                    dp[m] = min(dp[m], dp[m - c] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1