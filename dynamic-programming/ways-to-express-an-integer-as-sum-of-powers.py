class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        # m = int(n ** (1/x))
        m = 0
        while (m + 1) ** x <= n:
            m += 1
        
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for j in range(m + 1):
            dp[0][j] = 1

        for k in range(1, n + 1):
            dp[k][0] = 0

        for k in range(1, n + 1):
            for j in range(1, m + 1):  
                curr = j ** x

                if curr > k:
                    dp[k][j] = dp[k][j - 1]

                else:
                    dp[k][j] = (dp[k][j - 1] + dp[k - curr][j - 1]) % MOD

        
        return dp[n][m]