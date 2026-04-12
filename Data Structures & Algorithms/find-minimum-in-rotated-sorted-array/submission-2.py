class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums)
        left, right = 0, n-1
        small = float("inf")

        while left <= right:
            if nums[left] < nums[right]:
                small = min(small, nums[left])
                break
            mid = (left + right) // 2
            small = min(small, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1        


        return small



        