# Given an integer array nums, find a subarray that has the largest product, and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.

def maxProduct1(nums: list[int]) -> int:
    if len(nums) == 0:
        return False
    elif len(nums) == 1:
        return nums[0]

    OurMaxCurrent = nums[0]
    OurMinCurrent = nums[0]
    OurLargestProduct = nums[0]
    for index in range(1,len(nums)):
        OurCurrentProduct = (nums[index], nums[index] * OurMaxCurrent, nums[index] * OurMinCurrent)
        OurMaxCurrent, OurMinCurrent = max(OurCurrentProduct), min(OurCurrentProduct)
        OurLargestProduct = max(OurLargestProduct, OurMaxCurrent)
    return OurLargestProduct

nums = [-1,-2,-3,4,5,6,7,8,9,-10,-10,1,2,3]
print(maxProduct1(nums))