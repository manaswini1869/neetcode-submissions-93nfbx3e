class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visit):
            if (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in [[1,0], [-1,0],[0, 1],[0,-1]]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visit)


        for j in range(cols):
            dfs(0, j, pacific)
            dfs(rows-1, j, atlantic)

        
        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols-1, atlantic)
            

        return list(atlantic & pacific)



        