# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


def containsNearbyDuplicate1(nums: list[int], k: int) -> bool:
    OurDict = {}
    for i, value in enumerate(nums):
        if value in OurDict:
            if abs(OurDict[value] - i) <= k:
                return True
            else:
                OurDict[value] = i
        else:
            OurDict[value] = i
    return False

def containsNearbyDuplicate2(nums: list[int], k: int) -> bool:
    OurDict = {}
    for i, value in enumerate(nums):
        if value in OurDict and abs(OurDict[value] - i) <= k:
            return True
        else:
            OurDict[value] = i
    return False
V = [1,2,3,1]
k = 3

print(containsNearbyDuplicate1(V, k))
