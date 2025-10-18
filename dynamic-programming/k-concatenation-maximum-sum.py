class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        curr_max = best_max = arr[0]
        curr_sum = best_pref = arr[0]
        for num in arr[1:]:
            curr_max = max(num, num + curr_max)
            best_max = max(best_max, curr_max)

            curr_sum += num
            best_pref = max(best_pref, curr_sum)

        if k == 1:
            return max(best_max, 0) % MOD

        curr_sum = best_suf = arr[-1]
        for num in arr[::-1][1:]:
            curr_sum += num
            best_suf = max(best_suf, curr_sum)

        if curr_sum > 0:
            return max(best_max, k * curr_sum, best_pref + best_suf + (k - 2) * curr_sum, 0) % MOD
        else:
            return max(best_max, best_pref + best_suf, 0) % MOD
        
        