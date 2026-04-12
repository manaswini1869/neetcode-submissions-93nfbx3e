class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS, COLS = len(board), len(board[0])
        region = set()
        def dfs(r, c, curr_visit):
            if r < 0 or c < 0 or r == ROWS or c==COLS or (r, c) in region or board[r][c] == 'X':
                return 

            curr_visit.append((r, c))
            region.add((r, c))
            dfs(r+1, c, curr_visit)
            dfs(r-1, c, curr_visit)
            dfs(r, c-1, curr_visit)
            dfs(r, c+1, curr_visit)
   

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and (i, j) not in region:
                    visit = []
                    dfs(i, j, visit)
                    sour = True
                    for r, c in visit:
                        if r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1:
                            sour = False
                            break
                    if sour:
                        for r, c in visit:
                            board[r][c] = 'X'


        