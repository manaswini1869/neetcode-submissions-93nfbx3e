class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        num_0 = 0
        num_1 = 0

        for i in range(n):
            if i % 2 == 0:
                num_0 += nums[i]
            else:
                num_1 += nums[i]

        return max(num_0, num_1)
