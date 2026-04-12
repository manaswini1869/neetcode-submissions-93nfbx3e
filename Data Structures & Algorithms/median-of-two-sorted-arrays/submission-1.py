class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        resList = nums1 + nums2
        resList.sort()
        if len(resList) % 2 != 0:
            print(len(resList) % 2)
            return resList[len(resList)//2] 
        else:
            m = len(resList) // 2
            return (resList[m]+resList[m-1]) / 2
        