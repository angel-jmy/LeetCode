class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        N = len(arrivals)
        counts = defaultdict(int)
        min_disc = 0

        for i in range(N):
            if i < w:
                counts[arrivals[i]] += 1
            else:
                counts[arrivals[i]] += 1
                counts[arrivals[i - w]] -= 1

            while counts[arrivals[i]] > m:
                counts[arrivals[i]] -= 1
                min_disc += 1

        return min_disc
