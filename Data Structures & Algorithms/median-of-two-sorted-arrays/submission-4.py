class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        nums = nums1 + nums2

        nums.sort()

        n = len(nums)

        if n % 2 == 0:
            mid = n // 2
            return (nums[mid-1] + nums[mid] ) / 2
        else:
            return nums[n//2]

