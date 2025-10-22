class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.fstack = deque([])


    def visit(self, url: str) -> None:
        self.stack.append(url)
        self.fstack = deque([])
        

    def back(self, steps: int) -> str:
        for _ in range(steps):
            url = self.stack.pop()
            self.fstack.appendleft(url)
            if not self.stack:
                self.stack.append(url)
                self.fstack.popleft()
                break
                
        return self.stack[-1]
        

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.fstack:
                return self.stack[-1]

            url = self.fstack.popleft()
            self.stack.append(url)

        return self.stack[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)