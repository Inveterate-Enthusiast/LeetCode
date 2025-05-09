# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different
# size r x c keeping its original data.
#
# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns
# of the wanted reshaped matrix.
#
# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order
# as they were.
#
# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise,
# output the original matrix.
from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if (len(mat) * len(mat[0])) != (r * c):
            return mat
        result = [[0] * c for i in range(r)]
        _r, _c = 0, 0
        for row in mat:
            for num in row:
                result[_r][_c] = num

                if _c < (c-1):
                    _c +=1
                else:
                    _r += 1; _c = 0
        return result

mat = [[1,2],[3,4]]; r = 4; c = 1
x = Solution()
print(x.matrixReshape(mat, r, c))