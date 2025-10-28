class Solution:
    def balancedString(self, s: str) -> int:
        N = len(s)
        l, r = 0, 0
        counts = Counter(s)
        if all([v <= N // 4 for v in counts.values()]):
            return 0

        min_len = N + 1

        for r in range(N):
            counts[s[r]] -= 1
            while all([v <= N // 4 for v in counts.values()]) and l <= r:
                min_len = min(min_len, r - l + 1)
                counts[s[l]] += 1
                l += 1
            
        return min_len 

