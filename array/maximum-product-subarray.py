class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best_max = curr_max = nums[0]
        curr_min = nums[0]
        for num in nums[1:]:
            temp = curr_max
            curr_max = max(num, curr_max * num, curr_min * num)
            curr_min = min(num, temp * num, curr_min * num)

            best_max = max(best_max, curr_max)

        return best_max