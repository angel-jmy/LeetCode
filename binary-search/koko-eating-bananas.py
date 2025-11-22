class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        N = len(piles)
        def get_hours(k: int) -> int:
            total = 0
            for p in piles:
                # ceil(p / k) without float
                total += (p + k - 1) // k
            return total

        l, r = 1, max(piles)
        while l <= r:
            mid = l + (r - l) // 2
            hour = get_hours(mid)
            if hour > h:
                l = mid + 1
            else:
                r = mid - 1
        return l