# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
#
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row, col = len(matrix), len(matrix[0])
        if row <= 1 or col <= 1:
            return True

        # first cycle
        for i in range(row-1, -1, -1):
            temp_col = 0
            num = matrix[i][temp_col]
            for j in range(i+1, row):
                if (temp_col:=(temp_col + 1)) < col:
                    if num != matrix[j][temp_col]: return False

        # second cycle
        for i in range(col):
            temp_row = 0
            num = matrix[temp_row][i]
            for j in range(i+1, col):
                if (temp_row:=(temp_row + 1)) < row:
                    if matrix[temp_row][j] != num: return False

        return True


matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
x = Solution()
print(x.isToeplitzMatrix(matrix))