# You are given an m x n integer array grid.
# There is a robot initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
#
# An obstacle and space are marked as 1 or 0 respectively in grid.
# A path that the robot takes cannot include any square that is an obstacle.
#
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
# The testcases are generated so that the answer will be less than or equal to 2 * 109.

def uniquePathsWithObstacles1(obstacleGrid: list[list[int]]) -> int:
    OurMatrix = [[(None if obstacleGrid[i][j] == 1 else 0) for j in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
    for rowIndex in range(len(OurMatrix)):
        for columnIndex in range(len(OurMatrix[0])):
            if rowIndex == 0 and columnIndex == 0:
                OurMatrix[rowIndex][columnIndex] = 1 if OurMatrix[rowIndex][columnIndex] != None else 0
            elif rowIndex == 0:
                if OurMatrix[rowIndex][columnIndex] == None or OurMatrix[rowIndex][columnIndex-1] == 0:
                    OurMatrix[rowIndex][columnIndex] = 0
                else:
                    OurMatrix[rowIndex][columnIndex] = 1
            elif columnIndex == 0:
                if OurMatrix[rowIndex][columnIndex] == None or OurMatrix[rowIndex-1][columnIndex] == 0:
                    OurMatrix[rowIndex][columnIndex] = 0
                else:
                    OurMatrix[rowIndex][columnIndex] = 1
            else:
                if OurMatrix[rowIndex][columnIndex] == None:
                    OurMatrix[rowIndex][columnIndex] = 0
                else:
                    OurMatrix[rowIndex][columnIndex] = (OurMatrix[rowIndex-1][columnIndex]) + (OurMatrix[rowIndex][columnIndex-1])
    return OurMatrix[-1][-1]

obstacleGrid = [[0,0]]
print(uniquePathsWithObstacles1(obstacleGrid))