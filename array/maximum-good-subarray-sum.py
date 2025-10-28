class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        pref = 0 # Current pref
        max_sum = -float('inf')

        hashmap = {} # Best/minimum pref at a given number

        for i in range(N):
            num = nums[i]
            
            comp1 = num + k
            comp2 = num - k

            if comp1 in hashmap:
                cur_sum = pref + num - hashmap[comp1]
                max_sum = max(max_sum, cur_sum)

            if comp2 in hashmap:
                cur_sum = pref + num - hashmap[comp2]
                max_sum = max(max_sum, cur_sum)

            if num in hashmap:
                hashmap[num] = min(hashmap[num], pref)
            else:
                hashmap[num] = pref

            pref += num

        return max_sum if max_sum != -float('inf') else 0