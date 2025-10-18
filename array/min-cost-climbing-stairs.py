class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        N = len(cost)
        dp = [float('inf')] * (N + 1)

        dp[1] = 0
        dp[2] = min(cost[0], cost[1])

        for i in range(2, N):
            dp[i + 1] = min(dp[i - 1] + cost[i - 1], dp[i] + cost[i])

        return dp[N]

