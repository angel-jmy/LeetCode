class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.hashmap = defaultdict(list)
        for i, num in enumerate(arr):
            self.hashmap[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        indexes = self.hashmap[value]
        left_idx = bisect_left(indexes, left)
        right_idx = bisect_right(indexes, right)

        return right_idx - left_idx
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)