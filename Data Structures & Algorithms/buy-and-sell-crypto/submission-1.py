class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = float("-inf")
        buy = prices[0]
        n = len(prices)

        for i in range(1, n):
            profit = max(profit, prices[i]-buy)
            buy = min(buy, prices[i])
        
        return profit if profit > 0 else 0




        