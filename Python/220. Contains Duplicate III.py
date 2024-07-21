# You are given an integer array nums and two integers indexDiff and valueDiff.
#
# Find a pair of indices (i, j) such that:
#
# i != j,
# abs(i - j) <= indexDiff.
# abs(nums[i] - nums[j]) <= valueDiff, and
# Return true if such pair exists or false otherwise.
import math
def containsNearbyAlmostDuplicate1(nums: list[int], indexDiff: int, valueDiff: int) -> bool:
    for leftIndex in range(len(nums)):
        rightIndex = leftIndex
        while rightIndex == leftIndex or (rightIndex - leftIndex) != indexDiff:
            if abs(nums[rightIndex] - nums[leftIndex]) <= valueDiff and abs(rightIndex - leftIndex) <= indexDiff and rightIndex != leftIndex:
                return True
            rightIndex += 1
            if rightIndex > (len(nums)-1):
                rightIndex -= 1
                break
        if abs(nums[rightIndex] - nums[leftIndex]) <= valueDiff and abs(rightIndex - leftIndex) <= indexDiff and rightIndex != leftIndex:
            return True
    return False

def containsNearbyAlmostDuplicate2(nums: list[int], indexDiff: int, valueDiff: int) -> bool:
    if valueDiff < 0:
        return False
    bucket = {}
    for index, value in enumerate(nums):
        ind = value // (valueDiff + 1)
        if ind in bucket:
            return True
        if ind + 1 in bucket and abs(value - bucket[ind + 1]) <= valueDiff:
            return True
        if ind - 1 in bucket and abs(value - bucket[ind - 1]) <= valueDiff:
            return True
        bucket[ind] = value

        if len(bucket) > indexDiff:
            del bucket[nums[index - indexDiff] // (valueDiff + 1)]
    return False


def containsNearbyAlmostDuplicate3(nums: list[int], indexDiff: int, valueDiff: int) -> bool:
    if valueDiff < 0 or len(nums) <= 1:
        return False
    OurBasket = {}
    for index, value in enumerate(nums):
        basketIndex = math.floor(value / (valueDiff + 1))
        if basketIndex in OurBasket:
            return True
        if (basketIndex + 1) in OurBasket and abs(value - OurBasket[basketIndex + 1]) <= valueDiff:
            return True
        if (basketIndex - 1) in OurBasket and abs(value - OurBasket[basketIndex - 1]) <= valueDiff:
            return True
        OurBasket[basketIndex] = value
        #check length just after add new an element in OurBasket
        while len(OurBasket) > indexDiff:
            OurBasket.pop(math.floor(nums[index - indexDiff]/(valueDiff + 1)))
    return False





V = [1,5,9,1,5,9]
indexDiff = 2
valueDiff = 3
print(containsNearbyAlmostDuplicate3(V, indexDiff, valueDiff))




