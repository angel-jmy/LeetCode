class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums)
        curr_avg = sum(nums[:k]) / k
        max_avg = curr_avg

        for i in range(k, N):
            left = i - k
            curr_avg -= nums[left] / k
            curr_avg += nums[i] / k
            max_avg = max(max_avg, curr_avg)


        return max_avg

        