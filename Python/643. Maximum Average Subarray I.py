# You are given an integer array nums consisting of n elements, and an integer k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.

def findMaxAverage1(nums: list[int], k: int) -> float:
    CurrentSum = sum(nums[:k])
    MaxMeanValue = CurrentSum/k
    leftIndex = 0
    for rightIndex in range(k, len(nums)):
        if (rightIndex - leftIndex + 1) < k:
            continue
        while leftIndex <= rightIndex and (rightIndex - leftIndex + 1)!=k:
            CurrentSum -= nums[leftIndex]
            leftIndex += 1
        CurrentSum += nums[rightIndex]
        MaxMeanValue = max(MaxMeanValue, CurrentSum/k)
    return MaxMeanValue

def findMaxAverage1(nums: list[int], k: int) -> float:
    OurMaxAverage = None
    leftIndex = OurCurrentSum = 0
    for rightIndex in range(len(nums)):
        OurCurrentSum += nums[rightIndex]
        if (rightIndex - leftIndex + 1) < k:
            continue
        while leftIndex <= rightIndex and (rightIndex - leftIndex + 1) > k:
            OurCurrentSum -= nums[leftIndex]
            leftIndex += 1
        if (rightIndex - leftIndex + 1) == k:
            OurMaxAverage = max(OurMaxAverage, (OurCurrentSum/k)) if OurMaxAverage else (OurCurrentSum/k)

    return OurMaxAverage



nums = [-1]
k = 1
print(findMaxAverage1(nums, k))