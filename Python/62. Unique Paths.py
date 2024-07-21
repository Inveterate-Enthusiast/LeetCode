# There is a robot on an m x n grid.
# The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
# The test cases are generated so that the answer will be less than or equal to 2 * 109.


def uniquePaths1(m: int, n: int) -> int:
    OurMatrix = [[(1 if i*j==0 else 0) for j in range(n)] for i in range(m)]
    for rowIndex in range(1, len(OurMatrix)):
        for columnIndex in range(1, len(OurMatrix[0])):
            OurMatrix[rowIndex][columnIndex] = OurMatrix[rowIndex-1][columnIndex] + OurMatrix[rowIndex][columnIndex-1]
    return OurMatrix[m-1][n-1]

m = 1; n = 1
print(uniquePaths1(m, n))