# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.

def intersection1(nums1: list[int], nums2: list[int]) -> list[int]:
    resultList = []
    OurDict = {}
    for i, value in enumerate(nums1):
        OurDict[value] = i
    nums2 = list(set(nums2))
    for value in nums2:
        if value in OurDict:
            resultList.append(value)
    return resultList

def intersection2(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1).intersection(set(nums2)))
V1 = [1,2,2,1]
V2 = [2,2]

print(intersection2(V1, V2))