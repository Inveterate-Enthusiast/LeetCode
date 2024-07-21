# You are given an integer array nums and an integer k.
#
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
#
# Return the maximum number of operations you can perform on the array.

def maxOperations1(nums: list[int], k: int) -> int:
    OurDict = {}
    OurIndexList = []
    OurResultNumber = 0
    for index, value in enumerate(nums):
        if (k-value) in OurDict:
            OurIndexList.append(index)
            OurIndexList.append(OurDict[(k - value)][0])
            OurResultNumber += 1
            if len(OurDict[(k-value)]) > 1:
                OurDict[(k - value)].pop(0)
            else:
                del OurDict[(k-value)]
            continue
        if value not in OurDict:
            OurDict[value] = [index]
        else:
            OurDict[value].append(index)
    for index in sorted(OurIndexList, reverse= True):
        nums.pop(index)
    return OurResultNumber

# реализация через two pointers (удалять элементы не обязательно)
def maxOperations2(nums: list[int], k: int) -> int:
    OurResultNumber = 0
    nums = sorted(nums)
    leftIndex, rightIndex = 0, (len(nums)-1)
    while leftIndex < rightIndex:
        currentSum = nums[leftIndex] + nums[rightIndex]
        if currentSum == k:
            OurResultNumber += 1
            leftIndex += 1
            rightIndex -= 1
        elif currentSum < k:
            leftIndex += 1
        else:
            rightIndex -= 1

    return OurResultNumber


V = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
OurK = 3
print(maxOperations2(V, OurK))