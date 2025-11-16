class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)
        hashmap = defaultdict(list)
        for i, num in enumerate(nums):
            hashmap[num].append(i)

        def find_dist(idx):
            num = nums[idx]
            indexes = hashmap[num]
            M = len(indexes)
            if M == 1:
                return -1
            cur_idx = bisect_left(indexes, idx)

            if cur_idx > 0:
                left_idx = cur_idx - 1
                left_diff = indexes[cur_idx] - indexes[left_idx]
            else:
                left_idx = M - 1
                left_diff = indexes[cur_idx] + N - indexes[left_idx]

            if cur_idx < M - 1:
                right_idx = cur_idx + 1
                right_diff = indexes[right_idx] - indexes[cur_idx]
            else:
                right_idx = 0
                right_diff = indexes[0] + N - indexes[cur_idx]

            return min(left_diff, right_diff)

        res = []
        for q in queries:
            diff = find_dist(q)
            res.append(diff)

        return res
