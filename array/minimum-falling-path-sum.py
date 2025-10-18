class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0] = matrix[0].copy()

        for i in range(1, m):
            for j in range(n):
                l, middle, r = j - 1, j, j + 1
                candidates = [dp[i - 1][middle]]
                if l >= 0:
                    candidates.append(dp[i - 1][l])
                if r < n:
                    candidates.append(dp[i - 1][r])

                dp[i][j] = min(candidates) + matrix[i][j]
        
        return min(dp[m - 1])