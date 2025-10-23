class StockSpanner:

    def __init__(self):
        self.prices = []
        self.stack = [] # Stores the price and span so far
        

    def next(self, price: int) -> int:   
        span = 1     
        while self.stack and self.stack[-1][0] <= price:
            _, prev_span = self.stack.pop()
            span += prev_span
        
        self.stack.append((price, span))
        
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)