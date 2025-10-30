class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        N = len(nums)
        pref_min = [0] * N
        pref_min[0] = nums[0]
        suff_min = [0] * N
        suff_min[N - 1] = nums[N - 1]

        for i in range(1, N):
            pref_min[i] = min(pref_min[i - 1], nums[i])

        for i in range(N - 2, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])

        min_sum = float('inf')
        for j in range(1, N - 1):
            if pref_min[j - 1] < nums[j] and suff_min[j + 1] < nums[j]:
                min_sum = min(min_sum, pref_min[j - 1] + nums[j] + suff_min[j + 1])

        return min_sum if min_sum != float('inf') else -1

