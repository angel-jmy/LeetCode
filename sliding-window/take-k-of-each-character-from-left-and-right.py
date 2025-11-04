class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        N = len(s)
        if k == 0:
            return 0
        tot_count = Counter(s)
        if len(tot_count) < 3:
            return -1

        window = defaultdict(int)
        for c in ['a', 'b', 'c']:
            if tot_count[c] < k:
                return -1

        max_len = 0
        l = 0
        for r in range(N):
            window[s[r]] += 1
            while window['a'] > tot_count['a'] - k or window['b'] > tot_count['b'] - k or window['c'] > tot_count['c'] - k:
                if l <= r:
                    window[s[l]] -= 1
                    l += 1

            max_len = max(max_len, r - l + 1)

        return N - max_len