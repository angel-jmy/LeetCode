class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        hq = []
        items = 0
        for num in counts:
            heapq.heappush(hq, (counts[num], num))
            items += 1
            if items > k:
                heapq.heappop(hq)

        return [item[1] for item in hq]