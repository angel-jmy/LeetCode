class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        N = len(s)
        l, r = 0, 0
        counts = {}
        max_len = 0

        for r in range(N):
            c = s[r]
            while c in counts and counts[c] >= 2:
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    del counts[s[l]]

                l += 1

            counts[c] = counts.get(c, 0) + 1
            max_len = max(max_len, r - l + 1)

        return max_len