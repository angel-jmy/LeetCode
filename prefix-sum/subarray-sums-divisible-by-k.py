class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        cache = defaultdict(int)
        cache[0] = 1
        cur_sum = 0

        counter = 0

        for num in nums:
            cur_sum += num
            mod = cur_sum % k
            
            counter += cache[mod]
            cache[mod] += 1

        return counter
