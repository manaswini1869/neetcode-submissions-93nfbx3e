class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])


        def dfs(grid, visit, r, c):

            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == '0':
                return 1

            if grid[r][c] == '1':
                grid[r][c] = '0'
            
            visit.add((r, c))

            dfs(grid, visit, r+1, c)
            dfs(grid, visit, r-1, c)
            dfs(grid, visit, r, c+1)
            dfs(grid, visit, r, c-1)
            visit.remove((r, c))

            return 1

        islands = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    islands += dfs(grid, set(), i, j)

        return islands


