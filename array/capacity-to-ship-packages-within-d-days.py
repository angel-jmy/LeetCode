class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def get_days(cap):
            day = 1
            curr = 0
            for w in weights:
                curr += w
                if curr > cap:
                    day += 1
                    curr = w
            return day

        l, r = max(weights), sum(weights)
        while l <= r:
            mid = l + (r - l) // 2
            res = get_days(mid)
            # print(mid, res)
            if res > days:
                l = mid + 1
            else:
                r = mid - 1

        return l