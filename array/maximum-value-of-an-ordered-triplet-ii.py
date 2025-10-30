class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)
        pref_max = [0] * N
        suf_max = [0] * N

        pref_max[0] = nums[0]
        suf_max[N - 1] = nums[N - 1]

        for i in range(1, N):
            pref_max[i] = max(pref_max[i - 1], nums[i])

        for i in range(N - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], nums[i])

        max_val = -float('inf')
        for i in range(1, N - 1):
            max_val = max(max_val, (pref_max[i - 1] - nums[i]) * suf_max[i + 1])

        return max_val if max_val > 0 else 0