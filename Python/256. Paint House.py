# There is a row of n houses, where each house can be painted one of three colors:
# red, blue, or green.
# The cost of painting each house with a certain color is different.
# You have to paint all the houses such that no two adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.
#
# For example, costs[0][0] is the cost of painting house 0 with the color red;
# costs[1][2] is the cost of painting house 1 with color green, and so on...
# Return the minimum cost to paint all houses.

def minCost1(costs: list[list[int]]) -> int:
    Matrix = [[(0,0)]*(len(costs[0])) for _ in range(len(costs))]
    colourArray = ["r", "g", "b"]
    for rowIndex in range(len(Matrix)):
        firtsMin = (float("inf"), "")
        secondMin = (float("inf"), "")
        for columnIndex in range(len(Matrix[0])):
            if rowIndex == 0:
                Matrix[rowIndex][columnIndex] = (costs[rowIndex][columnIndex], colourArray[columnIndex])
            else:
                Matrix[rowIndex][columnIndex] = (costs[rowIndex][columnIndex] + (curFirstMin[0] if curFirstMin[1] != colourArray[columnIndex] else curSecondMin[0]), colourArray[columnIndex])

            if Matrix[rowIndex][columnIndex][0] < firtsMin[0]:
                secondMin = firtsMin
                firtsMin = Matrix[rowIndex][columnIndex]
            elif Matrix[rowIndex][columnIndex][0] < secondMin[0]:
                secondMin = Matrix[rowIndex][columnIndex]

        curFirstMin = firtsMin
        curSecondMin = secondMin

    return firtsMin[0]

costs = [[3,5,3],[6,17,6],[7,13,18],[9,10,18]]
print(minCost1(costs))