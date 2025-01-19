# Given a 2D integer array matrix, return the transpose of matrix.
#
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        result = [[None] * r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                result[j][i] = matrix[i][j]
        return result

matrix = [[1,2,3],[4,5,6]]
x = Solution()
print(x.transpose(matrix))