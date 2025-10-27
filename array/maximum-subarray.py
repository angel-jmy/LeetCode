class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cursum = maxsum
        for num in nums[1:]:
            cursum = max(cursum + num, num)
            maxsum = max(maxsum, cursum)

        return maxsum
        