class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        dp = [[0]* (target+1) for _ in range(n)]
        
        ops = [-1, +1]
        for i in range(n-1, -1, -1):
            for t in range(target+1):
                for op in ops:
                    if nums[i]*op == t:
                        dp[i][t] += 1

        return dp[0][target]