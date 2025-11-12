class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hq = []
        count = 0
        for num in nums:
            heapq.heappush(self.hq, num)
            count += 1
            if count > k:
                heapq.heappop(self.hq)
        


    def add(self, val: int) -> int:
        if not self.hq:
            heapq.heappush(self.hq, val)
            return val

        if val <= self.hq[0]:
            return self.hq[0]
        else:
            heapq.heappushpop(self.hq, val)
            return self.hq[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)