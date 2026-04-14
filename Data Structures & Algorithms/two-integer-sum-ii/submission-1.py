class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)
        left, right = 0, n-1
        while left < right:
            mid = (left + right) // 2
            if numbers[left] + numbers[mid] == target:
                return [left+1, mid+1]
            
            if numbers[left] + numbers[mid] > target:
                right = mid
            else:
                left = mid + 1



        