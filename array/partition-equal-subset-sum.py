class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # total = sum(nums)

        # if total % 2:
        #     return False

        # target = total // 2

        # cache = {0}

        # for num in nums:
        #     new_cache = cache.copy()
        #     for s in new_cache:
        #         if s + num == target:
        #             return True
        #         if s + num > target:
        #             continue
        #         else:
        #             cache.add(s + num)
            
        # return False


        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                if s - num < 0:
                    continue
                dp[s] = dp[s] or dp[s - num]

        return dp[target]