class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows, cols = len(board), len(board[0])
        for r in range(rows):
            rws, cls = set(), set()
            for c in range(cols):
                if board[r][c] != '.':
                    if board[r][c] in rws:
                        return False
                    
                    rws.add(board[r][c])
                if board[c][r] != '.':
                    if board[c][r] in cls:
                        return False
                    
                    cls.add(board[c][r])
        
        for s in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (s//3)*3 + i
                    col = (s%3)*3 + j
                    if board[row][col] != '.':
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])

        return True



        