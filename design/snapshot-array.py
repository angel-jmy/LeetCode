class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.arr = [[(0, 0)]] * length # (id, elem)
        # print(self.arr)

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        
    def get(self, index: int, snap_id: int) -> int:
        history = self.arr[index]
        N = len(history)
        l, r = 0, N - 1
        while l <= r:
            mid = l + (r - l) // 2
            if history[mid][0] > snap_id:
                r = mid - 1
            else:
                l = mid + 1
        return history[r][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)