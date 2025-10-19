class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_prof = 0
        for p in prices:
            max_prof = max(max_prof, p - min_price)
            min_price = min(min_price, p)

        return max_prof