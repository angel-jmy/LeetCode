class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums = [-num for num in nums]
        heapq.heapify(nums)

        score = 0
        k = min(k, N)

        for _ in range(k):
            num = -heapq.heappop(nums)
            score += num
            heapq.heappush(nums, -ceil(num / 3))

        return score
