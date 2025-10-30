class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        N = len(nums)
        if N < 3:
            return 0

        left = Counter(nums[:1])          # counts of [0]
        right = Counter(nums[2:])         # counts of [2..N-1]

        res = 0
        for j in range(1, N - 1):
            num = nums[j]
            res = (res + left[2*num] * right[2*num]) % MOD
            left[num] += 1
            if j + 1 < N:
                right[nums[j + 1]] -= 1

        return res