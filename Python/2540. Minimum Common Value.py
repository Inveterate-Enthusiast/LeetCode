# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays.
# If there is no common integer amongst nums1 and nums2, return -1.
#
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

def getCommon(nums1: list[int], nums2: list[int]) -> int:
    OurDict = {}
    numWithHiestValue = (nums1) if nums1[0] >= nums2[0] else (nums2)
    numWithLowestValue = (nums2) if nums2[0] < nums1[0] else (nums1)
    for i, value in enumerate(numWithLowestValue):
        OurDict[value] = i
    result = -1
    for i in range(len(numWithHiestValue)):
        if numWithHiestValue[i] in OurDict:
            result = numWithHiestValue[i]
            break
    return result

nums1 = [6,13,18,18,28,34,37,39,46,50,52,54,62,63,65,66,75,80,97,98]
nums2 = [10,13,13,19,27,33,40,41,43,46,56,61,69,72,78,79,82,88,91,94]

result = getCommon(nums1, nums2)
print(result)