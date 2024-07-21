# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
#
# A subarray is a contiguous part of the array.

def numSubarraysWithSum1(nums: list[int], goal: int) -> int:
    OurNumber = 0
    OurCurrentSum = 0
    leftIndex = 0
    for rightIndex in range(0,len(nums)):
        OurCurrentSum += nums[rightIndex]
        if OurCurrentSum < goal:
            continue
        while OurCurrentSum > goal:
            OurCurrentSum -= nums[leftIndex]
            leftIndex += 1
        if OurCurrentSum == goal:
            OurNumber += 1

        while rightIndex == (len(nums) - 1) and leftIndex <= rightIndex:
            OurCurrentSum -= nums[leftIndex]
            if OurCurrentSum == goal:
                OurNumber += 1
            leftIndex += 1

    return OurNumber

def numSubarraysWithSum2(nums: list[int], goal: int) -> int:
    OurNumber = 0
    for leftIndex in range(0,len(nums)):
        OurCurrentSum = 0
        for rightIndex in range(leftIndex, len(nums)):
            OurCurrentSum += nums[rightIndex]
            if OurCurrentSum > goal:
                break
            elif OurCurrentSum < goal:
                continue
            OurNumber += 1
    return OurNumber

def numSubarraysWithSum3(nums: list[int], goal: int) -> int:
    OurNumber = 0
    OurCurrentSum = 0
    OurDict = {0:1}

    for num in nums:
        OurCurrentSum += num
        if OurCurrentSum - goal in OurDict:
            OurNumber += OurDict[OurCurrentSum - goal]
        OurDict[OurCurrentSum] = OurDict.get(OurCurrentSum, 0) + 1
    return OurNumber

def numSubarraysWithSum4(nums: list[int], goal: int) -> int:
    OurNumber = 0
    OurCurrentSum = 0
    OurDict = {0:1}
    for num in nums:
        OurCurrentSum += num
        OurNumber += OurDict.get(OurCurrentSum - goal, 0)
        OurDict[OurCurrentSum] = OurDict.get(OurCurrentSum, 0) + 1

    return OurNumber


V = [1,0,1,0,1]
OurGoal = 1
print(numSubarraysWithSum4(V, OurGoal))