class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_diff = 0
        ranges = [[x[0], x[-1]] for x in arrays]
        ranges1 = sorted(ranges, key = lambda x: (x[0], x[1]))
        ranges2 = sorted(ranges, key = lambda x: (-x[1], -x[0]))

        return max(ranges1[-1][-1] - ranges1[0][0], ranges2[0][1] - ranges2[-1][0])