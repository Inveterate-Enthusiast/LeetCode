# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
#
# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        our_set = {i for i in range(1, len(matrix) + 1)}

        for i in matrix:
            temp_set = set(i)
            if not our_set <= temp_set:
                return False

        for j in range(len(matrix)):
            temp_set = set()
            for i in matrix:
                temp_set.add(i[j])
            if not our_set <= temp_set:
                return False

        return True

matrix = [[1,1,1],[1,2,3],[1,2,3]]
x = Solution()
print(x.checkValid(matrix))