# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.

import functools
def product(arr:list):
    return functools.reduce(lambda x, y: x*y, arr)


def productExceptSelf1(nums: list[int]) -> list[int]:
    OurResultList = []
    OurGeneralProduct = product(nums)
    for value in nums:
        OurResultList.append(OurGeneralProduct/value)

    return OurResultList

def productExceptSelf2(nums: list[int]) -> list[int]:
    OurResultList = []
    for index in range(len(nums)):
        OurResultList.append(\
            (product(nums[:index]) if index != 0 else 1)\
            *\
            (product(nums[index+1:]) if index != len(nums)-1 else 1)\
            )
    return OurResultList

def productExceptSelf3(nums: list[int]) -> list[int]:
    OurResultList = [None] * len(nums)
    OurLeftList = [None] * len(nums)
    OurRightList = [None] * len(nums)
    # create prefix products elements for left list
    for i in range(0, len(nums)):
        if i == 0:
            OurLeftList[0] = 1
        else:
            OurLeftList[i] = OurLeftList[i-1] * nums[i-1]

    # then crate prefix products elements for right list
    for i in range(len(nums)-1, -1, -1):
        if i == len(nums)-1:
            OurRightList[len(nums) - 1] = 1
        else:
            OurRightList[i] = OurRightList[i+1] * nums[i+1]

    # lest build result list with general products
    for i in range(len(nums)):
        OurResultList[i] = OurLeftList[i] * OurRightList[i]

    return OurResultList

def productExceptSelf4(nums: list[int]) -> list[int]:
    leftProduct = [0]*len(nums)
    rightProduct = [0]*len(nums)
    OurResultList = [0]*len(nums)
    for index in range(len(nums)):
        if index == 0:
            leftProduct[index] = 1
        else:
            leftProduct[index] = nums[index-1] * leftProduct[index-1]
    for index in range(len(nums)-1, -1, -1):
        if index == len(nums)-1:
            rightProduct[index] = 1
        else:
            rightProduct[index] = nums[index+1] * rightProduct[index+1]

    for index in range(len(nums)):
        OurResultList[index] = leftProduct[index] * rightProduct[index]
    return OurResultList

def productExceptSelf5(nums: list[int]) -> list[int]:
    leftPrefixProduct = [1] * len(nums)
    rightPrefixProduct = [1] * len(nums)
    OurResultList = [0] * len(nums)
    for index in range(len(nums)):
        if index != 0:
            leftPrefixProduct[index] = nums[index-1] * leftPrefixProduct[index-1]
    for index in range(len(nums)-1, -1, -1):
        if index != (len(nums)-1):
            rightPrefixProduct[index] = nums[index+1] * rightPrefixProduct[index+1]
    for index in range(len(nums)):
        OurResultList[index] = leftPrefixProduct[index] * rightPrefixProduct[index]
    return OurResultList

OurNums = [6,8,3,4]
print(productExceptSelf5(OurNums))
