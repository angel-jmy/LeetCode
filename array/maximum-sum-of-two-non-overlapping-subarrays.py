class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        N = len(nums)
        pref = [0] * (N + 1)
        for i in range(N):
            pref[i + 1] = pref[i] + nums[i]

        f_len, s_len = {}, {}
        for r in range(firstLen - 1, N):
            l = r - firstLen + 1
            f_len[(l, r)] = pref[r + 1] - pref[l]

        for r in range(secondLen - 1, N):
            l = r - secondLen + 1
            s_len[(l, r)] = pref[r + 1] - pref[l]

        max_sum = -float('inf')

        for pair1, val1 in f_len.items():
            fl, fr = pair1
            for pair2, val2 in s_len.items():
                sl, sr = pair2
                if sr < fl or sl > fr:
                    max_sum = max(max_sum, val1 + val2)
                else:
                    continue
        
        return max_sum