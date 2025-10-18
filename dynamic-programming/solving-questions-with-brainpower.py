class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        dp = [0] * (N + 1)  # dp[N] = 0 by default

        for i in range(N - 1, -1, -1):
            points, skip = questions[i]
            next_i = min(N, i + skip + 1)
            take = points + dp[next_i]
            notake = dp[i + 1]
            dp[i] = max(take, notake)

        return dp[0]