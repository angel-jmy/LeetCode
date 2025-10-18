class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0] = grid[0].copy()

        for i in range(1, m):
            for j in range(n):
                dp[i][j] = float('inf')
                for j0 in range(n):
                    prev = grid[i - 1][j0]
                    cost = moveCost[prev][j]
                    dp[i][j] = min(dp[i][j], dp[i - 1][j0] + grid[i][j] + cost)
        
        return min(dp[m-1])