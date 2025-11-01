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
            sum_right = total - (prefs[i - 1] if i > 0 else 0)

            left_ops = q * i - sum_left
            right_ops = sum_right - q * (N - i)
            res.append(left_ops + right_ops)

            # if q < nums[0]:
            #     ops = suffs[0] - q * N
            # elif idx + 1 < N:
            #     ops = q * (idx + 1) - prefs[idx] + suffs[idx + 1] - q * (N - idx - 1)
            # else:
            #     ops = q * (idx + 1) - prefs[idx]
            # res.append(ops)

        return res

