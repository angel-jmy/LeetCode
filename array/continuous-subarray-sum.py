class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        prefs = [0] * (N + 1)

        for i in range(1, N + 1):
            prefs[i] = prefs[i - 1] + nums[i - 1]

        print(prefs)

        l, r = 0, 0
        while l < N + 1:
            r = l + 1
            while r < N + 1:
                if prefs[r] - prefs[l] and (prefs[r] - prefs[l]) % k == 0:
                    print(l, r)
                    return True
                r += 1
            l += 1

        return False

        