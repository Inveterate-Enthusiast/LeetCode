# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
#
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

def isMonotonic1(nums: list[int]) -> bool:
    if len(nums) <= 2:
        return True

    i, j = 0, 1
    while i < (len(nums)-1) and j < (len(nums)-1) and nums[i] == nums[j]:
        i += 1; j += 1
    else:
        if nums[i] < nums[j]:
            OurFlag = True
        elif nums[i] > nums[j]:
            OurFlag = False
        else:
            return True

    for index in range(len(nums)):
        if index == 0:
            continue
        if (nums[index] < nums[index-1]) if OurFlag else (nums[index] > nums[index-1]):
            return False
    return True

nums = [1,1,1,1]
print(isMonotonic1(nums))