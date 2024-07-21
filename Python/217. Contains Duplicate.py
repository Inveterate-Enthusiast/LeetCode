# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate1(nums: list[int]) -> bool:
    numsSet = list(set(nums))
    return not (len(numsSet) == len(nums))

def containsDuplicate2(nums: list[int]) -> bool:
    OurDict = {}
    for i, value in enumerate(nums):
        if value in OurDict:
            return True
        else:
            OurDict[value] = i
    return False

def containsDuplicate3(nums: list[int]) -> bool:
    OurSet = set()
    for value in nums:
        if value in OurSet:
            return True
        else:
            OurSet.add(value)
    return False

V = [1,1,1,3,3,4,3,2,4,2]

print(containsDuplicate3(V))