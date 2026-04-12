class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1:
        #     return 1

        # if n == 2:
        #     return 2

        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # DP
        cache = [-1] * n
        def dp(k):
            if k >= n:
                return k == n
            if cache[k] != -1:
                return cache[k]
            cache[k] = dp(k+1) + dp(k+2)
            return cache[k]
        return dp(0)