class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        tot_len = len(stones)
        hq = [-s for s in stones]
        heapq.heapify(hq)

        while tot_len >= 2:
            y = -heapq.heappop(hq)
            x = -heapq.heappop(hq)
            # print(x, y)
            if x == y:
                tot_len -= 2
            else:
                heapq.heappush(hq, x - y)
                tot_len -= 1

        return -hq[0] if hq else 0