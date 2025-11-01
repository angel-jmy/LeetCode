class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        
        N = len(nums)
        left = Counter()
        right = Counter(nums[1:])

        prefs = [0] * N
        pref_map = defaultdict(int)
        pref_map[nums[0]] = 0
        for i in range(1, N):
            if nums[i] in pref_map:
                prefs[i] += pref_map[nums[i]]
                pref_map[nums[i]] += i
        
        suff_map = defaultdict(int)
        suff_map[nums[N - 1]] = N - 1
        suffs = [0] * N
        for i in range(N - 2, -1, -1):
            suffs[i] += suff_map[nums[i]]
            suff_map[nums[i]] += i

        print(prefs)
        print(suffs)

        arr = [0] * N
        for i in range(N):
            if i == 0:
                arr[i] = suffs[i] - i * right[nums[i]]
            elif i == N - 1:
                arr[i] = i * left[nums[i]] - prefs[i]
            else:
                arr[i] = suffs[i] - i * right[nums[i]] + i * left[nums[i]] - prefs[i]

            left[nums[i]] += 1
            if i + 1 < N and right[nums[i + 1]] > 0:
                right[nums[i + 1]] -= 1
        
        return arr