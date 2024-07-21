# Given an integer array nums and an integer k, return the maximum length
# of a subarray  that sums to k. If there is not one, return 0 instead.

def maxSubArrayLen1(nums: list[int], k: int) -> int:
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        if nums[0] == k:
            return 1
        else:
            return 0

    OurMaxLenght = 0
    OurDict = {}
    OurPrefixSum = 0

    for index, value in enumerate(nums):
        OurPrefixSum += value
        if OurPrefixSum == k:
            OurMaxLenght = index + 1
        elif OurPrefixSum - k in OurDict:
            OurMaxLenght = max(OurMaxLenght, index - OurDict[OurPrefixSum - k])
        if not OurPrefixSum in OurDict:
                OurDict[OurPrefixSum] = index

    return OurMaxLenght




OurNums = [1,1,0]
OurK = 1
print(maxSubArrayLen1(OurNums, OurK))