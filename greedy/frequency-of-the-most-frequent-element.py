class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        N = len(nums)
        if N == 1:
            return 1

        nums.sort()
        max_len = 1
        ops = 0
        l = 0
        for r in range(1, N):
            items = r - l
            ops += (nums[r] - nums[r - 1]) * items
            while ops > k and l < N:
                ops = (ops - (nums[r - 1] - nums[l])) // items
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len

            