# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        allowed_digits = {i for i in range(1, 9+1)}
        check_row, check_col, check_square = defaultdict(set), defaultdict(set), defaultdict(set)
        rows, cols = len(board), len(board[0])
        for row in range(0, rows):
            for col in range(0, cols):
                x = board[row][col]

                if x.isdigit():
                    x = float(x)
                    if not x in allowed_digits:
                        return False

                    if x in check_row[row]:
                        return False
                    else:
                        check_row[row].add(x)

                    if x in check_col[col]:
                        return False
                    else:
                        check_col[col].add(x)

                    square = (row // 3, col // 3)
                    if x in check_square[square]:
                        return False
                    else:
                        check_square[square].add(x)
                else:
                    continue

        return True

board = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

x = Solution()
print(x.isValidSudoku(board))