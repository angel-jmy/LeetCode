class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # N = len(nums)
        # dp = [float('inf')] * N
        # dp[0] = 0

        # for i in range(N):
        #     curr = nums[i]
        #     for j in range(curr + 1):
        #         if i + j < N:
        #             dp[i + j] = min(dp[i + j], dp[i] + 1)

        # return dp[N - 1]

        N = len(nums)
        if N < 2:
            return 0

        steps = 0
        end = 0          # end of current jump's window
        farthest = 0     # farthest we can reach while scanning this window

        # We only need to traverse up to N-2; once our window reaches N-1 we're done.
        for i in range(N - 1):
            # Expand the farthest reachable index within the current window
            if i + nums[i] > farthest:
                farthest = i + nums[i]

            # If we reached the end of the current window, we must take a jump
            if i == end:
                steps += 1
                end = farthest
                if end >= N - 1:
                    break

        return steps

        # N = len(nums)
        # dp = [float('inf')] * N
        # dp[0] = 0

        # r = 0  # rightmost index whose dp has been assigned
        # for i in range(N):
        #     if i > r:
        #         break  # unreachable, though the problem guarantees reachability
        #     curr = nums[i]
        #     reach = min(N - 1, i + curr)

        #     # Fill dp only for *newly* reachable positions (each index once).
        #     while r < reach:
        #         r += 1
        #         dp[r] = dp[i] + 1

        #     if r == N - 1:
        #         return dp[r]

        # return dp[N - 1]
