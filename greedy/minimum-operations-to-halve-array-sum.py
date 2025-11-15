class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        nums = [-num for num in nums]
        heapq.heapify(nums)

        reduced = 0
        ops = 0

        while reduced < total / 2:
            num = -heapq.heappop(nums)
            half = num / 2
            reduced += half
            ops += 1
            heapq.heappush(nums, -reduced)

        return ops
