class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = prices[:]
        N = len(prices)

        for i in range(N - 1, -1, -1):
            while stack and prices[i] < prices[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = prices[i] - prices[stack[-1]]
            
            stack.append(i)

        return res