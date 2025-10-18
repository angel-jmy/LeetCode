class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        dp = [0] + [float('inf')] * n
        costs = [0] + costs

        for i in range(1, n + 1):
            if i == 1:
                dp[i] = costs[i] + 1 + dp[i - 1]
            elif i == 2:
                dp[i] = min(costs[i] + 1 + dp[i - 1], costs[i] + 4 + dp[i - 2])
            else:
                dp[i] = min(costs[i] + 1 + dp[i - 1], costs[i] + 4 + dp[i - 2], costs[i] + 9 + dp[i - 3])
        
        return dp[n]