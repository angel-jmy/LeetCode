class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        dp = [[0] * (i + 1) for i in range(rows)]
        dp[0][0] = triangle[0][0]

        for i in range(1, rows):
            for j in range(i + 1):
                left_j, right_j = j - 1, j

                if left_j < 0:
                    dp[i][j] = dp[i - 1][right_j] + triangle[i][j]
                elif right_j >= i:
                    dp[i][j] = dp[i - 1][left_j] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][left_j], dp[i - 1][right_j]) + triangle[i][j]
        
        return min(dp[rows - 1])