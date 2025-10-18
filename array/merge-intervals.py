class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x: (x[0], x[1]))

        res = []
        size = 0

        for item in intervals:
            if size == 0:
                res.append(item)
                size += 1
            elif size > 0 and item[0] > res[size - 1][1]:
                res.append(item)
                size += 1
            elif size > 0 and item[0] <= res[size - 1][1]:
                res[size - 1][1] = max(res[size - 1][1], item[1])

        
        return res

        