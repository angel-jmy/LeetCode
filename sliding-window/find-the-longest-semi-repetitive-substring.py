class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        counts = defaultdict(int)
        N = len(s)
        l, r = 0, 0
        pairs = 0
        max_len = 0

        for r in range(N):
            counts[s[r]] += 1
            if counts[s[r]] >= 2:
                pairs += 1

            while pairs >= 2:
                left = s[l]
                if counts[left] == 2:
                    counts[left] -= 1
                    pairs -= 1
                    l += 1    
                else:
                    counts[left] -= 1
                    l += 1
            max_len = max(max_len, r - l + 1)

        return max_len

            


