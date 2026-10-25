class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix) 
        cols = len(matrix[0])

        for r in range(rows):
            left = 0
            right = cols - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[r][mid] == target:
                    return True
                elif matrix[r][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
        