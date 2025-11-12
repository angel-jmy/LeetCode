class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        N = len(nums)
        ops = 0

        while N >= 2:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            print(x, y)

            if x >= k:
                return ops

            heapq.heappush(nums, x * 2 + y)
            N -= 1
            ops += 1
        
        return ops
