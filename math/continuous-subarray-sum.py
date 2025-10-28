class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        cache = {0: -1} # Recording the index of the first seen MOD
        cur_sum = 0

        for i in range(N):
            cur_sum += nums[i]
            mod = cur_sum % k
            if mod in cache:
                if i - cache[mod] >= 2:
                    return True

            else:
                cache[mod] = i

        return False