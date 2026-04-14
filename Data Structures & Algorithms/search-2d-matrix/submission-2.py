class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            if matrix[i][0] <= target <= matrix[i][cols-1]:
                left, right = 0, cols-1
                while left <= right:
                    if matrix[left][right] == target:
                        return True
                    elif matrix[left][right] > target:
                        right -= 1
                    else:
                        left += 1

        return False



        