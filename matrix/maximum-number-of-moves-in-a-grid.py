class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 0

        for j in range(1, n):
            for i in range(m):
                best = -1
                for ni in (i-1, i, i+1):
                    if 0 <= ni < m and grid[ni][j-1] < grid[i][j] and dp[ni][j-1] != -1:
                        best = max(best, dp[ni][j-1] + 1)
                dp[i][j] = best

        ans = max(max(row) for row in dp)
        return max(ans, 0)
