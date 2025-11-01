class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
        prefs = [0] * N
        prefs[0] = nums[0]
        for i in range(1, N):
            prefs[i] = prefs[i - 1] + nums[i]

        suffs = [0] * N
        suffs[N - 1] = nums[N - 1]
        for i in range(N - 2, -1, -1):
            suffs[i] = suffs[i + 1] + nums[i]

        print(nums)
        print(prefs)
        print(suffs)
        
        def binary_search(target):
            l, r = 0, N - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return r

        print(binary_search(1))

        res = []
        for q in queries:
            # print(q)
            idx = binary_search(q)
            print(idx)
            if q < nums[0]:
                ops = suffs[0] - q * N
            elif idx + 1 < N:
                ops = q * (idx + 1) - prefs[idx] + suffs[idx + 1] - q * (N - idx - 1)
            else:
                ops = q * (idx + 1) - prefs[idx]
            res.append(ops)

        return res

