class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        target = sum(nums) - x
        if target == 0:
            return N
        prefix = {0: -1}
        curr = 0
        max_len = -1

        for i, num in enumerate(nums):
            curr += num
            if curr - target in prefix:
                max_len = max(max_len, i - prefix[curr - target])
            prefix[curr] = i

        return N - max_len if max_len != -1 else -1
        
        
        # N = len(nums)
        # l, r = 0, 0
        # diff = sum(nums) - x
        # if diff == 0:
        #     return N

        # curr_sum = 0

        # max_len = 0

        # for r in range(N):
        #     curr_sum += nums[r]
        #     while curr_sum > diff and l < N:
        #         curr_sum -= nums[l]
        #         l += 1

        #     if curr_sum == diff and l < N:
        #         max_len = max(max_len, r - l + 1)
        #         curr_sum -= nums[l]
        #         l += 1


        # return N - max_len if max_len != 0 else -1


        