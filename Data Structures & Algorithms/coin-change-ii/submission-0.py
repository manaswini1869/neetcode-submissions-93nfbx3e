class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        dp = {} # saving the coin, amount : unique_path so far

        def dfs(coin_index, collected_ammount):
            if coin_index > len(coins):
                return 0
            if dp[(coins[coin_index], collected_ammount)]:
                return dp[(coins[coin_index], collected_ammount)]

            for coin in coins:
                dp[(coins[coin_index], collected_ammount)] = 1 + dfs(coin_index+1, collected_amount+amount[coin_index])
                        

        return dfs(0, 0)


