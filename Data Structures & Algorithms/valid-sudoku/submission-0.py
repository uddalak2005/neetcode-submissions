class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in board:
            s = set()
            count = 0
            for j in i:
                if j != ".":
                    s.add(j)
                    count += 1


            if len(s) != count:
                return False

        for i in range(9):
            s = set()
            count = 0
            for j in range(9):
                if board[j][i] != ".":
                    s.add(board[j][i])
                    count += 1

            if len(s) != count:
                return False

        for row_block in range(0, 9, 3):
            for col_block in range(0, 9, 3):
                s = set()
                count = 0
                for j in range(row_block, row_block + 3):
                    for k in range(col_block, col_block + 3):
                        if board[j][k] != ".":
                            s.add(board[j][k])
                            count += 1
                if count != len(s):
                    return False

        return True
