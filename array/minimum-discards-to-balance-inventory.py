class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        N = len(arrivals)
        # counts = defaultdict(int)
        min_disc = 0
        dq = defaultdict(lambda: deque())

        for i in range(N):
            x = arrivals[i]
            while dq[x] and dq[x][0] < i - w + 1:
                dq[x].popleft()

            curr_count = len(dq[x])
            if curr_count < m:
                dq[x].append(i)
            elif curr_count == m:
                min_disc += 1

        return min_disc
