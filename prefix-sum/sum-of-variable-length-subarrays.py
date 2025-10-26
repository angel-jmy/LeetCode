class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        N = len(nums)
        pref = [0] * (N + 1)
        tot_sum = 0

        for i in range(N):
            num = nums[i]
            pref[i + 1] = pref[i] + num
            start = max(0, i - num)
            tot_sum += pref[i + 1] - pref[start]

        return tot_sum

