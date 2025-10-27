class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)
        M = len(queries)
        
        nums.sort()
        pref = [0] * (N + 1)

        for i in range(N):
            pref[i + 1] = pref[i] + nums[i]

        def binarySearch(target):
            l, r = 0, N
            while l <= r:
                mid = l + (r - l) // 2
                if pref[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            return r

        res = []
        for q in queries:
            res.append(binarySearch(q))

        return res
                