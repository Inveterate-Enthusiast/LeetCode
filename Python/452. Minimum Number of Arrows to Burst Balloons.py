# There are some spherical balloons taped onto a flat wall that represents the XY-plane.
# The balloons are represented as a 2D integer array points
# where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches
# between xstart and xend. You do not know the exact y-coordinates of the balloons.
#
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
# A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend.
# There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
#
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

def findMinArrowShots1(points: list[list[int]]) -> int: #долго по времени из-за сортировки выбором
    for index in range(len(points)):
        OurMinIndex = index
        for index2 in range(index, len(points)):
            if points[index2][0] < points[OurMinIndex][0]:
                OurMinIndex = index2
        if OurMinIndex != index:
            points[index], points[OurMinIndex] = points[OurMinIndex], points[index]
    newPoints = []
    newIndex = 0
    for index in range(len(points)):
        if index == 0:
            newPoints.append(points[index])
            newIndex = 0
            continue
        if newPoints[newIndex][1] >= points[index][0]:
            newPoints[newIndex][1] = points[index][1] if points[index][1] < newPoints[newIndex][1] else newPoints[newIndex][1]
            continue
        else:
            newPoints.append(points[index])
            newIndex += 1
    return len(newPoints)


def findMinArrowShots2(points: list[list[int]]) -> int:
    OurDict = {}
    for index in range(len(points)):
        if OurDict.get((points[index][0]), 0) == 0:
            OurDict[points[index][0]] = points[index][1]
        elif OurDict[points[index][0]] > points[index][1]:
            OurDict[points[index][0]] = points[index][1]
    OurDict = sorted(OurDict.items())
    newPoints = []
    newIndex = None
    for leftX, rightX in OurDict:
        if newIndex == None:
            newPoints.append([leftX, rightX])
            newIndex = 0
            continue
        if newPoints[newIndex][1] >= leftX:
            newPoints[newIndex][1] = rightX if rightX < newPoints[newIndex][1] else newPoints[newIndex][1]
            continue
        else:
            newPoints.append([leftX, rightX])
            newIndex += 1

    return len(newPoints)


OurPoints = [[1,9],[7,16],[2,5],[7,12],[9,11],[2,10],[9,16],[3,9],[1,3]]
print(findMinArrowShots2(OurPoints))