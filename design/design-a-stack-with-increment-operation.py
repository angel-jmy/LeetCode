class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize
        self.size = 0

    def push(self, x: int) -> None:
        if self.size < self.max_size:
            self.stack.append(x)
            self.size += 1

    def pop(self) -> int:
        if not self.stack:
            return -1
        self.size -= 1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        if k > self.size:
            k = self.size

        for i in range(k):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)