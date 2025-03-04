class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buying = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if (prices[i] < buying):
                buying = prices[i]
            elif prices[i] - buying > profit:
                profit = prices[i] - buying
        
        return profit