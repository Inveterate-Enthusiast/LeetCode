# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.

def minPathSum1(grid: list[list[int]]) -> int:
    OurMatrix = [[(grid[i][j] if i == j == 0 else 0) for j in range(len(grid[0]))] for i in range(len(grid))]
    for rowIndex in range(len(OurMatrix)):
        for columnIndex in range(len(OurMatrix[0])):
            if rowIndex == columnIndex == 0:
                continue
            if rowIndex == 0 or columnIndex == 0:
                OurMatrix[rowIndex][columnIndex] = grid[rowIndex][columnIndex] + OurMatrix[(rowIndex-1) if columnIndex == 0 else rowIndex][(columnIndex-1) if rowIndex == 0 else columnIndex]
            else:
                OurMatrix[rowIndex][columnIndex] = grid[rowIndex][columnIndex] + min(OurMatrix[rowIndex-1][columnIndex], OurMatrix[rowIndex][columnIndex-1])
    return OurMatrix[-1][-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum1(grid))