class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0] * (i + 1) for i in range(numRows)]

        dp[0][0] = 1

        for i in range(1, numRows):
            for j in range(i + 1):
                left_j = j - 1
                right_j = j
                if left_j < 0:
                    dp[i][j] = dp[i - 1][right_j]
                elif right_j >= i:
                    dp[i][j] = dp[i - 1][left_j]
                else:
                    dp[i][j] = dp[i - 1][left_j] + dp[i - 1][right_j]

        return dp