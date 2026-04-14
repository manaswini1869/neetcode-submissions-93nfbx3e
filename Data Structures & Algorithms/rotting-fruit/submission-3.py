class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        nei = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit = set()
            visit.add((r, c))
            time = 0
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                    for dx, dy in nei:
                        nx, ny = x+dx, y+dy
                        if min(nx, ny) < 0 or nx == ROWS or ny == COLS or grid[nx][ny] == 0 or (nx, ny) in visit:
                            continue
                        q.append((nx, ny))
                        visit.add((nx, ny))
                time += 1
            return time
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    count = bfs(i, j)

        return count-1 if count > 1 else -1


        