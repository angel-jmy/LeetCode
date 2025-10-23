class StockSpanner:

    def __init__(self):
        self.prices = []
        self.days = 0
        

    def next(self, price: int) -> int:        
        span = 0
        self.prices.append(price)
        self.days += 1
        N = self.days
       
        for i in range(N):
            if self.prices[i] <= price:
                span += 1
            else:
                span = 0
        
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)