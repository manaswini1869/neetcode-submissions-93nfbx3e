class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        dp = {} # saving the coin, amount : unique_path so far

        def dfs(coin_index, collected_amount):
            if collected_amount == amount:
                return 1
            if collected_amount > amount:
                return 0
            if coin_index >= len(coins):
                return 0
            if (coin_index, collected_amount) in  dp:
                return dp[(coin_index , collected_amount)]

            take = dfs(coin_index, collected_amount + coins[coin_index])
            skip = dfs(coin_index + 1, collected_amount)

            dp[(coin_index, collected_amount)] = take + skip

            return dp[(coin_index, collected_amount)]                        

        return dfs(0, 0)


