class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_max, best_max = nums[0], nums[0]
        curr_min, best_min = nums[0], nums[0]

        for num in nums[1:]:
            curr_max = max(num, curr_max + num)
            curr_min = min(num, curr_min + num)

            best_max = max(best_max, curr_max)
            best_min = min(best_min, curr_min)

        return max(abs(best_max), abs(best_min))
