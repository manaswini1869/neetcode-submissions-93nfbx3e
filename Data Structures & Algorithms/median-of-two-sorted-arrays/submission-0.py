class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        resList = nums1 + nums2
        resList.sort()
        print(resList)
        if len(resList) /2 != 0:
            return resList[len(resList)//2] 
        else:
            m = len(resList) // 2
            print(m)
            return (resList[m]+resList[m+1]) / 2
        return 1
        