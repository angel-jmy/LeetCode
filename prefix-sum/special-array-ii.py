class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        N = len(nums)
        pref = [0] * N

        for i in range(1, N):
            flag = nums[i] % 2 != nums[i - 1] % 2
            pref[i] = pref[i - 1] + flag

        res = []

        for l, r in queries:
            cursum = pref[r] - pref[l]
            length = r - l
            res.append(cursum == length)

        return res