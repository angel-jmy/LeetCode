class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        N = len(nums)
        res = []
        l = 0
        for r in range(N):
            if r > 0 and nums[r] - nums[r - 1] > 1:
                if r - 1 == l:
                    res.append(str(nums[l]))
                    l += 1
                else:
                    res.append(str(nums[l]) + "->" + str(nums[r - 1]))
                    l = r

        if l == N - 1:
            res.append(str(nums[l]))
        else:
            res.append(str(nums[l]) + "->" + str(nums[N - 1]))

        return res