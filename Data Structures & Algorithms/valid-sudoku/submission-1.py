class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows, cols = len(board), len(board[0])
        for r in range(rows):
            rws, cls = set(), set()
            for c in range(cols):
                if board[r][c] != '.':
                    if board[r][c] in rws:
                        return False
                    else:
                        rws.add(board[r][c])
                if board[c][r] != '.':
                    if board[c][r] in cls:
                        return False
                    else:
                        cls.add(board[c][r])
        
        i, j = 0, 0
        while i < rows and j < cols:
            box = set()
            for r in range(i, i+3):
                for c in range(j, j+3):
                    if board[r][c] != '.':
                        if board[r][c] in box:
                            return False
                        else:
                            box.add(board[r][c])
            i += 3
            j += 3

        return True



        