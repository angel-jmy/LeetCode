class MinStack:

    def __init__(self):
        self.stack = []
        self.pref_min = [2 ** 31 - 1]

    def push(self, val: int) -> None:
        if val < self.pref_min[-1]:
            self.pref_min.append(val)
        else:
            self.pref_min.append(self.pref_min[-1])
    
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.pref_min.pop()

        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.pref_min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()