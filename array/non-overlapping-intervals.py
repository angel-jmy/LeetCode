class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x: (x[0], x[1]))

        N = len(intervals)
        if N <= 1:
            return 0

        last_index = 0
        removed = 0

        for i in range(1, N):
            start, end = intervals[i][0], intervals[i][1]
            if start < intervals[last_index][1]:
                removed += 1
                if end < intervals[last_index][1]:
                    last_index = i
            else:
                last_index = i

        return removed
