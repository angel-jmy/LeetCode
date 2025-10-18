class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distances = [(x[0] ** 2 + x[1] ** 2) ** 0.5 for x in points]

        hq = []

        for d, (x, y) in zip(distances, points):
            heapq.heappush(hq, (d, x, y))

        res = []

        for _ in range(k):
            item = heapq.heappop(hq)
            res.append([item[1], item[2]])

        return res
        