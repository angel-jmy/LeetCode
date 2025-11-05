class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        max_freq = 0
        l = 0
        window = defaultdict(int)

        for r in range(N):
            window[nums[r]] += 1
            max_freq = max(max_freq, window[nums[r]])
            while r - l + 1 - max_freq > k:
                # if nums[l] == nums[r]:
                #     max_freq -= 1
                window[nums[l]] -= 1
                l += 1
            
        return max_freq