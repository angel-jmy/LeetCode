class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums)  # O(n)
        
        # Use a min-heap to keep the top k elements
        heap = []

        for num, freq in counts.items():  # O(m)
            heapq.heappush(heap, (freq, num))  # Push frequency first
            if len(heap) > k:
                heapq.heappop(heap)  # Pop the smallest frequency

        # Extract just the numbers from the heap
        return [num for freq, num in heap]