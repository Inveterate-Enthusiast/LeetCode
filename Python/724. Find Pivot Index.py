# Given an array of integers nums, calculate the pivot index of this array.
#
# The pivot index is the index
# where the sum of all the numbers strictly
# to the left of the index is equal to the sum of all the numbers strictly to the index's right.
#
# If the index is on the left edge of the array,
# then the left sum is 0 because there are no elements to the left.
# This also applies to the right edge of the array.
#
# Return the leftmost pivot index. If no such index exists, return -1.

def pivotIndex(nums: list[int]) -> int:
    leftPrefix = [0] * len(nums)
    rightPrifex = [0] * len(nums)
    OurResult = -1
    for index in range(0, len(nums)):
        if index == 0:
            leftPrefix[index] = nums[index]
        else:
            leftPrefix[index] = leftPrefix[index-1] + nums[index]
    for index in range(len(nums)-1, -1, -1):
        if index == (len(nums)-1):
            rightPrifex[index] = nums[index]
        else:
            rightPrifex[index] = rightPrifex[index+1] + nums[index]
    for index in range(len(nums)):
        if (leftPrefix[index-1] if index >=1 else 0) == (rightPrifex[index+1] if index <= (len(nums)-2) else 0):
            OurResult = index
            break

    return OurResult

V = [-1,-1,0,0,-1,-1]
print(pivotIndex(V))