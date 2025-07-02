# You are given an m x n matrix grid consisting of positive integers.
#
# Perform the following operation until grid becomes empty:
#
# Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
# Add the maximum of deleted elements to the answer.
# Note that the number of columns decreases by one after each operation.
#
# Return the answer after performing the operations described above.

from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            grid[row] = sorted(grid[row])

        result = 0
        for col in range(len(grid[0])):
            temp = float("-inf")
            for row in range(len(grid)):
                temp = max(temp, grid[row][col])
            result += temp

        return result

grid = [[1,2,4],[3,3,1]]
x = Solution()
print(x.deleteGreatestValue(grid))