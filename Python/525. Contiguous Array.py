# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

def findMaxLength1(nums: list[int]) -> int:
    if len(nums) == 0 or len(nums) == 1:
        return 0

    OurCurrentSum = 0
    OurDict = {}
    OurResultLength = 0
    for index, value in enumerate(nums):
        OurCurrentSum += 1 if value == 1 else (-1)
        if OurCurrentSum == 0:
            OurResultLength = index + 1
        elif OurCurrentSum in OurDict:
            OurResultLength = max(OurResultLength, index - OurDict[OurCurrentSum])
        else:
            OurDict[OurCurrentSum] = index


    return OurResultLength


def findMaxLength2(nums: list[int]) -> int:
    if len(nums) == 0 or len(nums) == 1:
        return 0
    OurPrefixSum = 0
    OurDict = {}
    OurMaxLenght = 0
    for index, value in enumerate(nums):
        if value == 1:
            OurPrefixSum += 1
        else:
            OurPrefixSum -= 1

        if OurPrefixSum == 0:
            OurMaxLenght = index + 1
        elif OurPrefixSum in OurDict:
            OurMaxLenght = max(OurMaxLenght, index - OurDict[OurPrefixSum])
        else:
            OurDict[OurPrefixSum] = index

    return OurMaxLenght



OurNums = [0, 0, 0, 1]
print(findMaxLength2(OurNums))