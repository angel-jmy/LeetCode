class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProf = 0

        for p in prices[1:]:
            maxProf = max(maxProf, p - minPrice)
            minPrice = min(minPrice, p)

        return maxProf