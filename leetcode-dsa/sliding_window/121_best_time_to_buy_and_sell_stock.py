class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        n = len(prices)
        left = 0

        for i in range(n-1):
            if prices[i+1] < prices[left]:
                left = i+1
                continue
            
            cur_profit = prices[i+1] - prices[left]
            max_profit = max(cur_profit, max_profit)

        return max_profit
            