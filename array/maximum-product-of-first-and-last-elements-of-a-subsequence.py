class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        N = len(nums)

        # Initialize prefix (allowed-left) extremes with index 0..m-1 (only index 0 is valid before first step,
        # so we start at j = m and seed with nums[0])
        left_max = nums[0]
        left_min = nums[0]
        ans = -float('inf')  # integer sentinel to avoid -inf float issues

        for j in range(m - 1, N):
            # Now expand the allowed-left prefix by including nums[j - m]
            v = nums[j - m + 1]
            if v > left_max:
                left_max = v
            if v < left_min:
                left_min = v

            # Combine current right with the best possible left
            x = nums[j]
            ans = max(ans, x * left_max, x * left_min)

        
        return ans