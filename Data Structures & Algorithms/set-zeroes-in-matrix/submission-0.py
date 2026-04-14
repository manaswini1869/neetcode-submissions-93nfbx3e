class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix)
        n = len(matrix[0])

        visited = set()

        for i in range(m):
            if 0 in matrix[i]:
                j = matrix[i].index(0)
                if (i, j) in visited:
                    continue
                else:
                    for k in range(n):
                        matrix[i][k] = 0
                    for k in range(m):
                        matrix[k][j] = 0
                        visited.add((k, j))



