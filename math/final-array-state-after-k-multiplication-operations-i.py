class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        hq = []
        N = len(nums)

        for idx, num in enumerate(nums):
            heapq.heappush(hq, (num, idx))

        for _ in range(k):
            num, idx = heapq.heappop(hq)
            heapq.heappush(hq, (num * multiplier, idx))

        res = [0] * N
        for _ in range(N):
            num, idx = heapq.heappop(hq)
            res[idx] = num

        return res
        