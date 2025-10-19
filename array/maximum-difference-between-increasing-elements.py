class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = 0
        curr_min = nums[0]
        for num in nums[1:]:
            max_diff = max(max_diff, num - curr_min)
            curr_min = min(curr_min, num)

        return max_diff if max_diff > 0 else -1