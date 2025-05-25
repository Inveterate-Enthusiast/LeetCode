# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2].
# Each integer appears exactly once except a which appears twice and b which is missing.
# The task is to find the repeating and missing numbers a and b.
#
# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        our_set = set(range(1, (n**2)+1))
        result = [0] * 2

        for i in range(n):
            for j in range(n):
                if grid[i][j] in our_set:
                    our_set.remove(grid[i][j])
                else:
                    result[0] = grid[i][j]

        result[1] = our_set.pop()
        return result

grid = [[1,3],[2,2]]
x = Solution()
print(x.findMissingAndRepeatedValues(grid))