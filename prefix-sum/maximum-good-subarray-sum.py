class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        pref = [0] * (N + 1)
        max_sum = -float('inf')

        hashmap = defaultdict(list)

        for i in range(N):
            num = nums[i]
            pref[i + 1] = pref[i] + num

            comp1 = num + k
            comp2 = num - k
            if comp1 in hashmap:
                for left in hashmap[comp1]:
                    cur_sum = pref[i + 1] - pref[left]
                    max_sum = max(max_sum, cur_sum)

            if comp2 in hashmap:
                for left in hashmap[comp2]:
                    cur_sum = pref[i + 1] - pref[left]
                    max_sum = max(max_sum, cur_sum)

            hashmap[num].append(i)

        return max_sum if max_sum != -float('inf') else 0