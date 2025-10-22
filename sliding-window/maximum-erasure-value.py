class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, 0
        max_sum = curr_sum = 0
        seen = set()
        for r in range(N):
            while nums[r] in seen:
                curr_sum -= nums[l]
                seen.remove(nums[l])
                l += 1


            seen.add(nums[r])
            curr_sum += nums[r]
            max_sum = max(max_sum, curr_sum)

        return max_sum
