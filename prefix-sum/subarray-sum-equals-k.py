class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = {}
        cache[0] = 1
        res = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            res += cache.get(curr_sum - k, 0)
            cache[curr_sum] = cache.get(curr_sum, 0) + 1

        return res