class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        costs = [abs(ord(c1) - ord(c2)) for c1, c2 in zip(s, t)]
        l, r = 0, 0
        max_len = 0
        tot_cost = 0

        for r in range(N):
            tot_cost += costs[r]
            while tot_cost > maxCost:
                tot_cost -= costs[l]
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len