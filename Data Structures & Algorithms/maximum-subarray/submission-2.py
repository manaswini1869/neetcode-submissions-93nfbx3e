class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)

        max_sum = sum(nums)

        l, r = 0, n-1
        while l <= r:
            max_sum = max(max_sum, sum(nums[l:r+1]))

            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1
        return max_sum


        