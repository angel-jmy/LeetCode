class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_diff = 0
        ranges = [[x[0], x[-1]] for x in arrays]
        ranges.sort(key = lambda x: (x[0], x[1]))

        return ranges[-1][-1] - ranges[0][0]