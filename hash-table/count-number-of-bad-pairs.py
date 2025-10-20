class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        hashmap = {}
        N = len(nums)
        for i in range(N):
            diff = nums[i] - i
            hashmap[diff] = hashmap.get(diff, 0) + 1

        good_pairs = 0
        for diff in hashmap:
            n = hashmap[diff]
            good_pairs += n * (n - 1) // 2

        total_pairs = N * (N - 1) // 2

        return total_pairs - good_pairs