# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.

def moveZeroes1(nums: list[int]) -> None:
    OurIndexList = []
    for index in range(len(nums)):
        if nums[index] == 0:
            OurIndexList.append(index)
            nums.append(0)
    nums[:] = [element for index, element in enumerate(nums) if index not in OurIndexList]
    pass

def moveZeroes2(nums: list[int]) -> None:
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1


V = [0,1,0,3,12]
moveZeroes2(V)
print(V)