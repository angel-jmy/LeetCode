class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(nums1)
        ab_sum = 0
        max_diff = 0
        max_idx = 0
        for i in range(N):
            diff = abs(nums1[i] - nums2[i])
            if diff > max_diff:
                max_diff = diff
                max_idx = i
            ab_sum += diff

        if ab_sum == 0:
            return 0

        target = nums2[max_idx]
        nums1.sort()
        idx = bisect_left(nums1, target)
        if idx >= N:
            idx = N - 1
        elif idx > 0:
            if target - nums1[idx - 1] < nums1[idx] - target:
                idx = idx - 1
        
        ab_sum -= max_diff
        ab_sum += abs(target - nums1[idx])

        return ab_sum