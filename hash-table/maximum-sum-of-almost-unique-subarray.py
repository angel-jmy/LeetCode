class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        N = len(nums)
        n_not_unique = 0
        curr_sum = max_sum = 0
        counts = defaultdict(int)
        for num in nums[:k]:
            if num not in counts:
                counts[num] += 1
            else:
                n_not_unique += 1
                counts[num] += 1
            curr_sum += num

        if n_not_unique <= k - m:
            max_sum = max(max_sum, curr_sum)

        for i in range(k, N):
            left = i - k
            if nums[left] == nums[i]:
                continue

            if counts[nums[left]] >= 2:
                counts[nums[left]] -= 1
                n_not_unique -= 1
            else:
                del counts[nums[left]]
            
            if nums[i] in counts:
                n_not_unique += 1
            
            counts[nums[i]] += 1

            curr_sum = curr_sum + nums[i] - nums[left]

            if n_not_unique <= k - m:
                max_sum = max(max_sum, curr_sum)

        return max_sum
        

