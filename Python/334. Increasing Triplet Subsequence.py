# Given an integer array nums, return true if there exists a triple of indices (i, j, k)
# such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

def increasingTriplet1(nums: list[int]) -> bool:
    if len(nums) <= 2:
        return False

    OurFlag = False
    MinFromLeft = []
    MaxFromRight = [0]*len(nums)
    for index in range(len(nums)):
        if index == 0:
           MinFromLeft.append(nums[index])
        else:
            MinFromLeft.append(min(MinFromLeft[index-1], nums[index]))
    for index in range(len(nums)-1, -1, -1):
        if index == (len(nums)-1):
            MaxFromRight[index] = nums[index]
        else:
            MaxFromRight[index] = max(MaxFromRight[index+1], nums[index])

    for index in range(len(nums)):
        if index != 0 and index != (len(nums)-1):
            if MinFromLeft[index-1] < nums[index] < MaxFromRight[index+1]:
                OurFlag = True
                break
    return OurFlag



V = [20,100,10,12,5,13]
print(increasingTriplet1(V))