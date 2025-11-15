class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        # total = sum(nums)
        heapq.heapify(nums)
        
        for _ in range(k):
            val = heapq.heappop(nums)
            heapq.heappush(nums, val + 1)

        return prod(nums) % MOD