class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        tot_num = sum(gifts)
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        
        i = 0
        while i < k:
            g = -heapq.heappop(gifts)
            r = isqrt(g)
            heapq.heappush(gifts, -r)
            tot_num -= g - r
            i += 1

        return tot_num

        