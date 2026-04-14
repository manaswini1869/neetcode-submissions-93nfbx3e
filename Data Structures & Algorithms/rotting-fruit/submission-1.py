class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        q = deque()
        fresh = 0
        minutes = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        while q:
            for _ in range(len(q)):
                x, y, minutes = q.popleft()

                if grid[r][c] == 0:
                    return minutes

                for dx, dy in directions:
                    if (0<= x+dx < rows and 0 <= y+dy < cols and grid[x+dx][y+dy] == 1):
                        grid[x+dx][y+dy] = 2
                        q.append((x+dx, y+dy, minutes + 1))
                        fresh -= 1

        return -1 if fresh > 0 else minutes

