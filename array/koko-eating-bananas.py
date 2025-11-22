class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        N = len(piles)
        def get_hours(k):
            eaten = 0
            curr = [0] * N
            hrs = 0
            while eaten < total:
                for i in range(N):
                    to_eat = min(piles[i] - curr[i], k)
                    if to_eat:
                        hrs += 1
                    curr[i] += to_eat
                    eaten += to_eat

            return hrs

        l, r = 1, max(piles)
        while l <= r:
            mid = l + (r - l) // 2
            hour = get_hours(mid)
            if hour > h:
                l = mid + 1
            else:
                r = mid - 1
        return l