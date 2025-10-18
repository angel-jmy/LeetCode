class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # ######### With map-based DP
        # N = len(nums)

        # cache = {}
        # cache[0] = 1

        # for num in nums:
        #     new_cache = {}
        #     for s, w in cache.items():
        #         new_cache[s + num] = new_cache.get(s + num, 0) + w
        #         new_cache[s - num] = new_cache.get(s - num, 0) + w

        #     cache = new_cache


        # return cache.get(target, 0)


        ####### With array-based DP
        total = sum(nums)
        N = len(nums)
        if (total + target) % 2 or abs(target) > total:
            return 0

        P = (total + target) // 2

        dp = [0] * (P + 1)

        dp[0] = 1

        for num in nums:
            for s in range(P, num - 1, -1):
                if s - num < 0:
                    continue

                dp[s] += dp[s - num]

        return dp[P]



        #### With Backtracking
        # N = len(nums)

        # # Quick infeasibility check
        # total = sum(nums)
        # if total < abs(target):
        #     return 0

        # # suffix_sum[i] = sum(nums[i:])
        # suffix_sum = [0] * (N + 1)
        # for i in range(N - 1, -1, -1):
        #     suffix_sum[i] = suffix_sum[i + 1] + nums[i]

        # memo = {}

        # def backtrack(idx, cur_sum):
        #     # Prune: even using all remaining numbers can't close the gap
        #     if abs(target - cur_sum) > suffix_sum[idx]:
        #         return 0

        #     if idx == N:
        #         return 1 if cur_sum == target else 0

        #     key = (idx, cur_sum)
        #     if key in memo:
        #         return memo[key]

        #     res = backtrack(idx + 1, cur_sum + nums[idx]) + \
        #           backtrack(idx + 1, cur_sum - nums[idx])

        #     memo[key] = res
        #     return res

        # return backtrack(0, 0)