class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for l in range(len(nums)):
            r = l + k
            temp = nums[l:r]
            if len(temp) == k:
                res.append(max(nums[l:r]))
        print(res)
        return res