class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(list)
        N = len(nums)
        for i in range(N):
            hashmap[nums[i]].append(i)

        arr = [0] * N
        for i in range(N):
            temp = hashmap[nums[i]]
            if len(temp) > 1:
                arr[i] = sum([i - idx if idx <= i else idx - i for idx in temp])

        return arr