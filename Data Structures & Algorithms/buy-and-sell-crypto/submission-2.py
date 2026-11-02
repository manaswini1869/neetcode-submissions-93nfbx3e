class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = float("-inf")
        n = len(prices)

        left = prices[0]

        for i in range(1, n):
            curr_profit = prices[i] - left
            if curr_profit > 0:
                profit = max(profit, curr_profit)
            
            left = min(left, prices[i])
        
        return 0 if profit == float("-inf") else profit


        