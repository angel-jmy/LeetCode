class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = Counter(words)

        hq = []
        # length = 0

        for w, f in counts.items():
            heapq.heappush(hq, (-f, w))
            # length += 1
            # if length > k:
            #     heapq.heappop(hq)
            #     length -= 1
        
        # hq = [w for f, w in sorted(hq, key = lambda x: (-x[0], x[1]))]

        return [heapq.heappop(hq)[1] for _ in range(k)]