class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        N = len(prices)
        pref = [0] * (N + 1)
        for i in range(N):
            pref[i + 1] = pref[i] + prices[i] * strategy[i]

        base = pref[N]
        maxprof = base

        win_prof = 0
        for i in range(k):
            if i >= k // 2:
                win_prof += prices[i]

        orig_prof = pref[k] - pref[0]
        delta = win_prof - orig_prof
        maxprof = max(maxprof, base + delta)

        for i in range(k, N):
            mid = i - k // 2
            win_prof -= prices[mid]
            win_prof += prices[i]
            orig_prof = pref[i + 1] - pref[i - k + 1]
            delta = win_prof - orig_prof
            maxprof = max(maxprof, base + delta)

        return maxprof