# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
#
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

def findDifference1(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    Our1Set = set(nums1)
    Our2Set = set(nums2)
    OurResultList = [[], []]
    for value in Our1Set:
        if value not in Our2Set:
            OurResultList[0].append(value)
    for value in Our2Set:
        if value not in Our1Set:
            OurResultList[1].append(value)
    return OurResultList

#более простой способ
def findDifference2(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    return [list((set(nums1)) - set(nums2)), list((set(nums2)) - (set(nums1)))]

nums1 = [1,2,3,3]; nums2 = [1,1,2,2]
print(findDifference2(nums1, nums2))