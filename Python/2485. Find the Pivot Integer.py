# Given a positive integer n, find the pivot integer x such that:
#
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

import math

def pivotInteger1(n: int) -> int:
    OurX = n
    OurList = []
    OurList.append(0)
    for i in range(1, n+1):
        OurList.append(OurList[i-1] + i)
    while OurList[OurX] != (OurList[n] - OurList[OurX-1]) and OurX > 1:
        OurX -= 1
    else:
        if OurList[OurX] == OurList[n] - OurList[OurX-1]:
            pass
        else:
            OurX = -1

    return OurX

OurN = 16
print(pivotInteger1(OurN))