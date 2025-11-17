class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        for l in range(N):
            if nums[l] == 1:
                break
        else:
            return True

        for r in range(l + 1, N):
            if nums[r] == 1:
                if r - l - 1 < k:
                    return False
                l = r

        return True