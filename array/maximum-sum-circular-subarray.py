class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max = curr_min = nums[0]
        one_max = curr_max
        one_min = curr_min
        total = curr_max
        neg_flag = curr_min < 0
        for num in nums[1:]:
            curr_max = max(num, num + curr_max)
            curr_min = min(num, num + curr_min)
        
            one_max = max(one_max, curr_max)
            one_min = min(one_min, curr_min)

            neg_flag = neg_flag and num < 0
            total += num
   
        if neg_flag: ### VERY IMPORTANT!!
            return max(nums)

        return max(one_max, total - one_min)
        