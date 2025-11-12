class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hq = []
        self.count = 0
        self.k = k
        for num in nums:
            heapq.heappush(self.hq, num)
            self.count += 1
            if self.count > k:
                heapq.heappop(self.hq)
                self.count -= 1
        


    def add(self, val: int) -> int:
        if self.count < self.k:
            heapq.heappush(self.hq, val)
            self.count += 1
            return val

        # if not self.hq:
        #     heapq.heappush(self.hq, val)
            
        if val <= self.hq[0]:
            return self.hq[0]
        else:
            heapq.heappushpop(self.hq, val)
            return self.hq[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)