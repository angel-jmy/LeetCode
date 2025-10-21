class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        avg = [-1] * N
        first_i = k
        if first_i + k > N - 1:
            return avg

        avg[first_i] = sum(nums[first_i - k:first_i + k + 1]) / (2 * k + 1)

        for i in range(first_i + 1, N - k):
            left = i - k - 1
            right = i + k
            avg[i] = avg[i - 1] + (nums[right] - nums[left]) / (2 * k + 1)

        return [int(num) for num in avg]