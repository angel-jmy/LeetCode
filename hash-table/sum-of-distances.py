class Solution:
    def distance(self, nums: List[int]) -> List[int]:        
        N = len(nums)
        arr = [0] * N
        
        left = defaultdict(int)
        left[nums[0]] = 1
        pref_map = defaultdict(int)
        pref_map[nums[0]] = 0
        for i in range(1, N):
            arr[i] += i * left[nums[i]] - pref_map[nums[i]]
            pref_map[nums[i]] += i
            left[nums[i]] += 1
        
        del left

        right = defaultdict(int)
        right[nums[N - 1]] = 1
        suff_map = defaultdict(int)
        suff_map[nums[N - 1]] = N - 1
        for i in range(N - 2, -1, -1):
            arr[i] += suff_map[nums[i]] - i * right[nums[i]]
            suff_map[nums[i]] += i
            right[nums[i]] += 1

        
        return arr