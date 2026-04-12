class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        MAX_AREA = 0
        def dfs(grid, visit, r, c):
            nonlocal MAX_AREA 
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            area = 1
            area += dfs(grid, visit, r+1, c)
            area += dfs(grid, visit, r-1, c)
            area += dfs(grid, visit, r, c-1)
            area += dfs(grid, visit, r, c+1)
            MAX_AREA = max(MAX_AREA, area)

            return area

        
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    dfs(grid, set(), i, j)
        
        return MAX_AREA if MAX_AREA != float("-inf") else 0