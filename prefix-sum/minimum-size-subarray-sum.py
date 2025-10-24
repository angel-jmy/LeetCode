class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, 0
        curr_sum = 0
        min_len = N + 1

        for r in range(N):
            curr_sum += nums[r]
            while curr_sum >= target:
                min_len = min(min_len, r - l + 1)
                curr_sum -= nums[l]
                l += 1

        return min_len if min_len != N + 1 else 0