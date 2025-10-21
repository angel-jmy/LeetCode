class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        i = j = 0
        max_len = 0
        for j in range(N):
            while nums[j] > k * nums[i]:
                i += 1
            max_len = max(max_len, j - i + 1)

        return N - max_len

