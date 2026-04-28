class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in row_set:
                    return False
                else:
                    row_set.add(board[i][j])
                if board[j][i] != "." and board[j][i] in col_set:
                    return False
                else:
                    col_set.add(board[j][i])   

        for s in range(9):
            curr = set()
            for i in range(3):
                for j in range(3):
                    r = (s//3)*3+i
                    c = (s%3)*3+j
                    if board[r][c] != "." and board[r][c] in curr:
                        return False
                    else:
                        curr.add(board[r][c])

        return True
        


        