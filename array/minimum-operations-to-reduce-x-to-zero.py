class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        l, r = 0, 0
        diff = sum(nums) - x
        curr_sum = 0

        max_len = 0

        while r < N:
            curr_sum += nums[r]
            while curr_sum > diff and l < N:
                curr_sum -= nums[l]
                l += 1

            if curr_sum == diff and l < N:
                max_len = max(max_len, r - l + 1)
                curr_sum -= nums[l]
                l += 1

            r += 1

        return N - max_len if max_len != 0 else -1


        