class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        ans = 1
        start = 0
        n = len(nums)
        
        for i in range(1, n):
            if nums[i-1] == nums[i]:
                start += 1
                continue
            if nums[i-1] != nums[i] - 1:
                start = i
            ans = max(ans, i - start + 1)
        return ans

