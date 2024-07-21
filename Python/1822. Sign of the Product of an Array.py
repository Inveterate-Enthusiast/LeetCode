# There is a function signFunc(x) that returns:
#
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.
#
# Return signFunc(product).


def arraySign1(nums: list[int]) -> int:
    OurNumber = 1
    for digit in nums:
        if digit == 0:
            return 0
        OurNumber *= digit
    return (-1) if OurNumber < 0 else 1

nums = [1,5,0,2,-3]
print(arraySign1(nums))