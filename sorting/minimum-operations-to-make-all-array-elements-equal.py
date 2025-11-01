class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
        prefs = [0] * N
        prefs[0] = nums[0]
        for i in range(1, N):
            prefs[i] = prefs[i - 1] + nums[i]

        total = prefs[-1]


        res = []
        for q in queries:
            # print(q)
            i = bisect_right(nums, q)
            sum_left = prefs[i - 1] if i > 0 else 0
            sum_right = total - sum_left

            left_ops = q * i - sum_left
            right_ops = sum_right - q * (N - i)
            res.append(left_ops + right_ops)

        return res

