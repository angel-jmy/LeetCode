class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l, r = 0, 0
        counts = defaultdict(int)
        max_len = 0

        for r in range(N):
            while counts[nums[r]] >= k:
                counts[nums[l]] -= 1
                l += 1

            counts[nums[r]] += 1
            max_len = max(max_len, r - l + 1)

        return max_len