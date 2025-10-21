class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        curr_sum = max_sum = 0
        counts = defaultdict(int)
        extras = 0
        for num in nums[:k]:
            curr_sum += num
            if num in counts:
                extras += 1
            
            counts[num] += 1

        if not extras:
            max_sum = max(max_sum, curr_sum)

        for i in range(k, N):
            left = i - k
            if nums[left] == nums[i]:
                continue
            
            if counts[nums[left]] >= 2:
                extras -= 1
                counts[nums[left]] -= 1
            else:
                del counts[nums[left]]

            if nums[i] in counts:
                extras += 1
            counts[nums[i]] += 1

            curr_sum = curr_sum + nums[i] - nums[left]

            if not extras:
                max_sum = max(max_sum, curr_sum)

        return max_sum
