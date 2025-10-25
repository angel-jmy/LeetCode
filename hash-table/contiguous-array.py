class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        curr_sum = 0
        hashmap = {0:-1}
        max_len = 0

        for r in range(N):
            if nums[r] == 1:
                curr_sum += 1
            else:
                curr_sum -= 1

            if curr_sum not in hashmap:
                hashmap[curr_sum] = r
            elif curr_sum in hashmap:
                l = hashmap[curr_sum]
                max_len = max(max_len, r - l)

        return max_len
            
