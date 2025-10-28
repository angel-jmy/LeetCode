class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        cache = defaultdict(int) # Stores the bit XOR prefix
        cache[0] = 1
        curr_pref = 0
        res = 0

        for i in range(N):
            curr_pref = curr_pref ^ nums[i]
            res += cache[curr_pref]
            cache[curr_pref] += 1

        return res
