# Given a 2D matrix matrix, handle multiple queries of the following type:
#
# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:
#
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements
# of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.
from typing import Optional, List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._matrix = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]
        for i in range(1, len(self._matrix)):
            for j in range(1, len(self._matrix[0])):
                self._matrix[i][j] = sum([
                    + self._matrix[i-1][j],
                    + self._matrix[i][j-1],
                    - self._matrix[i-1][j-1],
                    + matrix[i-1][j-1]
                ])


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        cur_sum = sum([
            self._matrix[row2+1][col2+1],
            - self._matrix[row1][col2+1],
            - self._matrix[row2+1][col1],
            + self._matrix[row1][col1]
        ])
        return cur_sum


X = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(X.sumRegion(1,1,2,2))
