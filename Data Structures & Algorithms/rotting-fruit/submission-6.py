class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        nei = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        fresh = 0

        def bfs(q):
            nonlocal fresh
            visit = set()
            time = 0
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    visit.add((x, y))
                    for dx, dy in nei:
                        nx, ny = x+dx, y+dy
                        if min(nx, ny) < 0 or nx == ROWS or ny == COLS or grid[nx][ny] == 0 or (nx, ny) in visit:
                            continue
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            fresh -= 1
                        q.append((nx, ny))
                        visit.add((nx, ny))
                time += 1
            return time
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        time = bfs(q)
        
        return time-1 if fresh == 0 else -1


        