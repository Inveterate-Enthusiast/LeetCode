# Given an integer array nums, find the subarray with the largest sum, and return its sum.


def maxSubArray1(nums: list[int]) -> int:
    OurDict = {0: 0}
    if len(nums) == 0:
        return False

    for i, value in enumerate(nums):
        OurDict[i+1] = value + OurDict[i]

    if len(OurDict) >= 2:
        for key, value in OurDict.items():
            if key == 0 :
                OurMinValue, OurMaxValue = value, value
                OurMinKey, OurMaxKey = key, key
            else:
                if value < OurMinValue:
                    OurMinValue = value
                    OurMinKey = key
                elif value > OurMaxValue:
                    OurMaxValue = value
                    OurMaxKey = key
        OurLargestSum = (OurDict[OurMaxKey] - OurDict[OurMinKey]) if OurDict[OurMaxKey] > max(nums) else max(nums)
    else:
        OurLargestSum = nums[0]

    return OurLargestSum

def maxSubArray2(nums: list[int]) -> int:
    if len(nums) == 0:
        return False
    elif len(nums) == 1:
        return nums[0]

    OurList = []
    OurList.append(nums[0])
    OurLargestSum = nums[0]

    for index in range(1,len(nums)):
        OurList.append(max((OurList[index-1] + nums[index]), nums[index]))
        OurLargestSum = OurList[index] if OurList[index] > OurLargestSum else OurLargestSum
    return OurLargestSum




nums = [-1000,-900,-800,1,2,-100,4,5,6]
print(maxSubArray2(nums))