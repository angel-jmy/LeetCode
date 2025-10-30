class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(nums)
        prefs = [defaultdict(int)] * N
        suffs = [defaultdict(int)] * N

        prefs[0][nums[0]] = 1
        suffs[0][nums[N - 1]] = 1

        for i in range(1, N):
            prefs[i] = prefs[i - 1].copy()
            prefs[i][nums[i]] += 1

        for i in range(N - 2, -1, -1):
            suffs[i] = suffs[i + 1].copy()
            suffs[i][nums[i]] += 1

        res = 0
        for j in range(1, N - 1):
            num = nums[j]
            res = (res + prefs[j - 1][num * 2] * suffs[j + 1][num * 2]) % MOD

        return res