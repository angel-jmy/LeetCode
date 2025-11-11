class SmallestInfiniteSet:

    def __init__(self):
        self.hq = []
        self.current = 1
        self.num_set = set()
        # self.num_set = set(num for num in range(1, 1001))

    def popSmallest(self) -> int:
        if self.hq:
            num = heapq.heappop(self.hq)
            self.num_set.remove(num)
        else:
            num = self.current
            self.current += 1
        return num
        

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.num_set:
            heapq.heappush(self.hq, num)
            self.num_set.add(num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)