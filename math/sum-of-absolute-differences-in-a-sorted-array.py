class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefs = [0] * N
        suffs = [0] * N
        prefs[0] = nums[0]
        suffs[N - 1] = nums[N - 1]
        for i in range(1, N):
            prefs[i] = prefs[i - 1] + nums[i]

        for i in range(N - 2, -1, -1):
            suffs[i] = suffs[i + 1] + nums[i]


        result = [0] * N
        for i in range(N):
            if i == 0:
                result[i] = suffs[i + 1] - (N - 1) * nums[i]
            elif i == N - 1:
                result[i] = (N - 1) * nums[i] - prefs[i - 1]
            else:
                result[i] = i * nums[i] - prefs[i - 1] + suffs[i + 1] - (N - i - 1) * nums[i]

        return result