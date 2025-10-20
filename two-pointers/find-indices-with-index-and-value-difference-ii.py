class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        N = len(nums)
        if indexDifference > N - 1:
            return [-1, -1]

        curr_max = curr_min = nums[0]
        max_idx = min_idx = 0

        for j in range(indexDifference, N):
            left = j - indexDifference
            if nums[left] > curr_max:
                curr_max = nums[left]
                max_idx = left
            if nums[left] < curr_min:
                curr_min = nums[left]
                min_idx = left

            if abs(nums[j] - curr_max) >= valueDifference:
                return [max_idx, j]
            
            if abs(nums[j] - curr_min) >= valueDifference:
                return [min_idx, j]

        return [-1, -1]