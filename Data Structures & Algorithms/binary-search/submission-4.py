class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)

        right = n-1
        left = 0

        mid = (right + left) // 2
        if nums[mid] == target:
            return mid

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1

        return -1
        
        




