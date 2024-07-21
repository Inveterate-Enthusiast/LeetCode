# Given a triangle array, return the minimum path sum from top to bottom.
#
# For each step, you may move to an adjacent number of the row below.
# More formally, if you are on index i on the current row,
# you may move to either index i or index i + 1 on the next row.

def minimumTotal1(triangle: list[list[int]]) -> int:
    if len(triangle) == 1:
        return triangle[0][0]
    OurMinResult = float("inf")
    for indexFloor in range(1, len(triangle)):
        for index in range((len(triangle[indexFloor]))):
            triangle[indexFloor][index] = triangle[indexFloor][index] + min(
                (triangle[indexFloor-1][index]) if index < len(triangle[indexFloor-1]) else float("inf"),
                (triangle[indexFloor-1][index-1]) if index-1 >= 0 else float("inf"))
            if indexFloor == (len(triangle) - 1):
                OurMinResult = min(OurMinResult, triangle[indexFloor][index])
    return OurMinResult

triangle = [[-10]]
print(minimumTotal1(triangle))