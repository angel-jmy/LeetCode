class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        pairs = 0
        for i in range(len(nums)):
            seen[nums[i]] += 1
        
        for n in seen.values():
            pairs += n * (n - 1) // 2

        return pairs