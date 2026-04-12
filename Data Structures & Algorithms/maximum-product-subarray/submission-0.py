class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        
        for i in range(n):
            curr = 1
            for j in range(i, n):
                curr *= nums[j]
                res = max(res, curr)

        return res
