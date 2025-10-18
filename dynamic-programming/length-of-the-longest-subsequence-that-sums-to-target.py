class Solution(object):
    def lengthOfLongestSubsequence(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        sums = {0:0}
        
        for i in range(1, N + 1):
            new_sum = sums.copy()
            for s, l in sums.items():
                if s + nums[i - 1] > target:
                    continue
               
                new_sum[s + nums[i - 1]] = max(new_sum.get(s + nums[i - 1], 0), l + 1)
                
            sums = new_sum.copy()

        return sums.get(target, -1)


        # if sum(nums) < target:
        #     return -1

        # # dp[s] = max length of subsequence that sums to s
        # dp = [-1] * (target + 1)
        # dp[0] = 0

        # for x in nums:
        #     # traverse backwards to avoid reusing the same element
        #     for s in range(target, x - 1, -1):
        #         if dp[s - x] != -1:
        #             dp[s] = max(dp[s], dp[s - x] + 1)

        # return dp[target]