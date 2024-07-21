# You have a long flowerbed in which some of the plots are planted,
# and some are not. However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
# return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    if n == 0:
        return True
    OurPrefixSum = 0
    leftIndex = 0
    OurFlag = False
    for rightIndex in range(len(flowerbed)):
        OurPrefixSum += flowerbed[rightIndex]
        if (rightIndex-leftIndex+1) < 3:
            if rightIndex > 0 and OurPrefixSum == 0:
                n -= 1
                flowerbed[(rightIndex + leftIndex) // 2] = 1
                OurPrefixSum += 1
                if n == 0:
                    OurFlag = True
                    break
            continue
        while leftIndex <= rightIndex and (rightIndex-leftIndex+1) > 3:
            OurPrefixSum -= flowerbed[leftIndex]
            leftIndex += 1
        if OurPrefixSum == 0:
            n -= 1
            flowerbed[(rightIndex + leftIndex) // 2] = 1
            OurPrefixSum += 1
            if n == 0:
                OurFlag = True
                break
    else:
        if len(flowerbed) > 1 and (flowerbed[rightIndex] == 0 and flowerbed[rightIndex-1] == 0):
            n -= 1
            if n == 0:
                OurFlag = True
        elif len(flowerbed) == 1 and OurPrefixSum == 0:
            OurFlag = True
    return OurFlag

flowerbed = [0]
n = 1

print(canPlaceFlowers(flowerbed, n))