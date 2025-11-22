class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def get_trips(t):
            trips = [t // ti for ti in time]
            return sum(trips)

        l = 1
        r = totalTrips * max(time)
        while l <= r:
            mid = l + (r - l) // 2
            tot_trips = get_trips(mid)
            if tot_trips < totalTrips:
                l = mid + 1
            else:
                r = mid - 1
        
        return l 
        