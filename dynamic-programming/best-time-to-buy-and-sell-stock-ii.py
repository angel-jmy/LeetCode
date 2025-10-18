class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprof = 0
        if len(prices) <= 1:
            return maxprof
        
        
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                maxprof += prices[i+1] - prices[i]
                
        return maxprof
                    