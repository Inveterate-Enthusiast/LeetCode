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

def getRow2(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        result = list()
        for i in range(rowIndex + 1):
            result.append(list())
            for j in range(i + 1):
                result[i].append(list())
                if j == 0 or j == i:
                    result[i][j] = 1
                else:
                    result[i][j] = result[i-1][j-1] + result[i-1][j]
        else:
            return result[i]

print(getRow2(1))