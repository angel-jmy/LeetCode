class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        prefs = [0] * (N + 1)

        for i in range(1, N + 1):
            prefs[i] = (prefs[i - 1] + nums[i - 1]) % k

        mods = defaultdict(list)
        for i in range(N + 1):
            new_mod = prefs[i]
            if new_mod in mods:
                if i - mods[new_mod][0] >= 2:
                    return True

            mods[new_mod].append(i)

        return False
            

