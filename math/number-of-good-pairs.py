class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        res = 0
        for num in counts:
            n = counts[num]
            res += n * (n - 1) // 2

        return res