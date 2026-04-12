class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit = set()
            visit.add((r, c))
            length = 0
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()

                    if grid[x][y] > length:
                        grid[x][y] = length
                    nei = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for dx, dy in nei:
                        if min((dx+x), (dy+y)) < 0 or dx + x >= ROWS or dy + y >= COLS or grid[dx+x][dy+y] == -1 or (dx+x, dy+y) in visit:
                            continue
                        q.append((dx+x, dy+y))
                        visit.add((dx+x, dy+y)) 
                length += 1                 
                
        


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    count = bfs(i, j)
        

