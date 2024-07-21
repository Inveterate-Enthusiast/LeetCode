# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

def getRow1(rowIndex: int) -> list[int]:
    OurTriangle = []
    for floorIndex in range(rowIndex+1):
        OurTriangle.append([1] * (floorIndex+1))
        if floorIndex == 0:
            continue
        for cellIndex in range(len(OurTriangle[floorIndex])):
            if cellIndex != 0 and cellIndex != (len(OurTriangle[floorIndex]) - 1):
                OurTriangle[floorIndex][cellIndex] = OurTriangle[floorIndex-1][cellIndex-1] + OurTriangle[floorIndex-1][cellIndex]
    return OurTriangle[rowIndex]

print(getRow1(1))