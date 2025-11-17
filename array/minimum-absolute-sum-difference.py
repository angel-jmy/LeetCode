class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10 ** 9 + 7
        if nums1 == nums2:
            return 0
        N = len(nums1)
        max_red = 0
        combined = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        combined.sort(key = lambda x: x[0])
        nums1 = [n1 for n1, n2 in combined]
        nums2 = [n2 for n1, n2 in combined]
        def find_closest(t):            
            idx = bisect_left(nums1, t)
            if idx >= N:
                idx = N - 1
            elif idx > 0:
                if t - nums1[idx - 1] < nums1[idx] - t:
                    idx = idx - 1
            return idx
        
        for i in range(N):
            idx = find_closest(nums2[i])
            if i == idx:
                continue
            red = abs(nums2[i] - nums1[i]) - abs(nums2[i] - nums1[idx])
            max_red = max(max_red, red)

     
        ab_sum = (sum([abs(nums1[i] - nums2[i]) for i in range(N)]) - max_red) % MOD

        return ab_sum