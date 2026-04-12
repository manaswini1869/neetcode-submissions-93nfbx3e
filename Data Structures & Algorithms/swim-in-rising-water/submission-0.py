class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        min_h = [[grid[0][0], 0, 0]] # time, r, c

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visit.add((0, 0))

        while min_h:
            t, r, c = heapq.heappop(min_h)

            if r == n-1 and c == n-1:
                return t

            for dx, dy in directions:
                neiR, neiC = r + dx, c + dy
                if (neiR < 0 or neiC < 0 or neiR == n or neiC == n or (neiR, neiC) in visit):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(min_h, [max(t, grid[neiR][neiC]), neiR, neiC])