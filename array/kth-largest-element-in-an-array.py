class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hq = []
        for num in nums:
            heapq.heappush(hq, -num)

        for i in range(k - 1):
            heapq.heappop(hq)

        return -heapq.heappop(hq)