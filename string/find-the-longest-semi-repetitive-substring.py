class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        counts = defaultdict(int)
        N = len(s)
        l, r = 0, 0
        max_len = 0
        pairs = 0

        for r in range(N):
            if r > 0 and s[r] == s[r - 1]:
                pairs += 1

            while pairs > 1:
                if l + 1 <= r and s[l] == s[l + 1]:
                    pairs -= 1
                    l += 1
                else:
                    l += 1

            max_len = max(max_len, r - l + 1)

        return max_len


