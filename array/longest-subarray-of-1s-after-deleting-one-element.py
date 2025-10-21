class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, 0
        max_len = 0

        # deleted = 0
        last_idx = -1

        for r in range(N):
            if nums[r] == 0 and last_idx == -1:
                last_idx = r
            elif nums[r] == 0 and last_idx >= 0:
                l = last_idx + 1
                last_idx = r

            max_len = max(max_len, r - l)

        return max_len