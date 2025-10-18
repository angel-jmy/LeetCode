class Solution(object):
    def countTexts(self, pressedKeys):
        """
        :type pressedKeys: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(pressedKeys)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            c = pressedKeys[i - 1]
            limit = 4 if c in '79' else 3
            
            for j in range(1, limit + 1):
                if i - j < 0 or pressedKeys[i - j] != c:
                    break
                dp[i] = (dp[i] + dp[i - j]) % MOD

        return dp[n]



        
