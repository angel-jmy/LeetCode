class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + (i + 1) * (j + 1) + waitCost[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + (i + 1) * (j + 1) + waitCost[i][j]
                
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + (i + 1) * (j + 1) + waitCost[i][j]

        return dp[m - 1][n - 1] - waitCost[m - 1][n - 1]