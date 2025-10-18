class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        buy, sell = [-float("inf")] * (k + 1), [0] * (k + 1)
        
        for i in range(days):
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j - 1] - prices[i])
                sell[j] = max(sell[j], buy[j] + prices[i])
        
        return sell[k]