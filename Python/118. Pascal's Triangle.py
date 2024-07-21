# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


def generate1(numRows: int) -> list[list[int]]:
    if numRows == 1:
        return [[numRows]]
    OurTriangle = [[1]]
    for floorIndex in range(1, numRows):
        OurTriangle.append([0]*(len(OurTriangle[floorIndex-1])+1))
        for cellIndex in range(len(OurTriangle[floorIndex])):
            if cellIndex == 0 or cellIndex == (len(OurTriangle[floorIndex])-1):
                OurTriangle[floorIndex][cellIndex] = 1
            else:
                OurTriangle[floorIndex][cellIndex] = OurTriangle[floorIndex-1][cellIndex-1] + OurTriangle[floorIndex-1][cellIndex]
    return OurTriangle

def generate2(numRows: int) -> list[list[int]]:
    OurTrangle = []
    for floorIndex in range(numRows):
        OurTrangle.append([1] * (floorIndex+1))
        if floorIndex == 0:
            continue
        for cellIndex in range(len(OurTrangle[floorIndex])):
            if cellIndex != 0 and cellIndex != (len(OurTrangle[floorIndex]) - 1):
                OurTrangle[floorIndex][cellIndex] = OurTrangle[floorIndex-1][cellIndex-1] + OurTrangle[floorIndex-1][cellIndex]
    return OurTrangle



print(generate1(5))