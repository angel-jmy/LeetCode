class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        N, M = len(houses), len(heaters)
        def get_covered(r):
            counter = 0
            # covered = set()
            i = j = 0
            while j < M:
                lb = heaters[j] - r
                ub = heaters[j] + r
                while i < N and houses[i] < lb:
                    i += 1
                while i < N and houses[i] >= lb and houses[i] <= ub:
                    counter += 1
                    i += 1
                j += 1
            return counter

        l, r = 0, max(heaters[M - 1] - houses[0], houses[N - 1] - heaters[0])
        while l <= r:
            mid = l + (r - l) // 2
            counts = get_covered(mid)
            if counts < N:
                l = mid + 1
            else:
                r = mid - 1

        return l