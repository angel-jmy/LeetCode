class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 1:
            return nums[0]
            
        dp1 = [0] * N
        dp2 = [0] * (N + 1)

        dp1[1], dp2[1] = nums[0], 0


        for i in range(2, N + 1):
            
            dp2[i] = max(dp2[i-1], dp2[i - 2] + nums[i - 1])

            if i < N:
                dp1[i] = max(dp1[i-1], dp1[i - 2] + nums[i - 1])


        return max(dp1[N-1], dp2[N])



        