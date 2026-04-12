class Solution:
    def findMin(self, nums: List[int]) -> int:
        inR = float('infinity')
        for i in nums:
            if i < inR:
                inR = i
        return inR