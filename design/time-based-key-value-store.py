class TimeMap:

    def __init__(self):
        self.values = dict()        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.values:
            self.values[key].append((timestamp, value))
        else:
            self.values[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""

        values = self.values[key]
        N = len(values)
        l, r = 0, N - 1

        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1

        if r < 0:
            return ""

        return values[r][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)