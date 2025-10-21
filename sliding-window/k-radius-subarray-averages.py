class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        avg = [-1] * N
        first_i = k
        if first_i + k > N - 1:
            return avg

        window_sum = sum(nums[first_i - k:first_i + k + 1])
        avg[first_i] = window_sum // (2 * k + 1)

        for i in range(first_i + 1, N - k):
            left = i - k - 1
            right = i + k
            window_sum = window_sum + nums[right] - nums[left]
            avg[i] = window_sum // (2 * k + 1)

        return avg