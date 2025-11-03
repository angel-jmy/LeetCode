class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        arr2 = nums + nums
        total = sum(nums)
        curr_ones = sum(arr2[:total])
        max_ones = curr_ones

        for i in range(1, N):
            curr_ones += arr2[i + total - 1]
            curr_ones -= arr2[i - 1]
            max_ones = max(max_ones, curr_ones)

        return total - max_ones

