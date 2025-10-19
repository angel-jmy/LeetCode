class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[defaultdict(lambda: float('-inf')) for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i > 0:
                    for k, v in dp[i - 1][j].items():
                        dp[i][j][k] = max(dp[i][j][k], v + coins[i][j])
                        if coins[i][j] < 0 and k < 2:
                            dp[i][j][k + 1] = max(dp[i][j][k + 1], v)

                if j > 0:
                    for k, v in dp[i][j - 1].items():          
                        dp[i][j][k] = max(dp[i][j][k], v + coins[i][j])
                        if coins[i][j] < 0 and k < 2:
                            dp[i][j][k + 1] = max(dp[i][j][k + 1], v)
                
        
        return max(dp[m - 1][n - 1].values())
                
                                        
