class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cache = {0:1}
        cursum = 0
        counter = 0

        for num in nums:
            cursum += num
            counter += cache.get(cursum - goal, 0)
            cache[cursum] = cache.get(cursum, 0) + 1

        return counter