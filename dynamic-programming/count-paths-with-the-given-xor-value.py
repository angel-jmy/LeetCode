class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[defaultdict(int) for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = 1
        for i in range(1, m):
            val = grid[i][0]
            for prev_xor, count in dp[i - 1][0].items():
                new_xor = prev_xor ^ val
                dp[i][0][new_xor] = (dp[i][0][new_xor] + count) % MOD

        for j in range(1, n):
            val = grid[0][j]
            for prev_xor, count in dp[0][j - 1].items():
                new_xor = prev_xor ^ val
                dp[0][j][new_xor] = (dp[0][j][new_xor] + count) % MOD

        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                for prev_xor, count in dp[i - 1][j].items():
                    new_xor = prev_xor ^ val
                    dp[i][j][new_xor] = (dp[i][j][new_xor] + count) % MOD
                for prev_xor, count in dp[i][j - 1].items():
                    new_xor = prev_xor ^ val
                    dp[i][j][new_xor] = (dp[i][j][new_xor] + count) % MOD

        return dp[m - 1][n - 1][k]
