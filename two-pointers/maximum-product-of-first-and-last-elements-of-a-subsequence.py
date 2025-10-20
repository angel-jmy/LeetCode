class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        N = len(nums)
        max_prod = -float('inf')

        for i in range(N - m):
            for j in range(i + m - 1, N):
                prod = nums[i] * nums[j]
                max_prod = max(max_prod, prod)

        return max_prod