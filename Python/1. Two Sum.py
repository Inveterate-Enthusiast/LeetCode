# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
from collections import defaultdict
from typing import List


def twoSum(nums: list[int], target: int) -> list[int]:
    OurIndicesList = []
    for index in range(len(nums)):
        if (nums[index] > target) if target >= 0 else (nums[index] < target):
            continue
        elif not (target - nums[index]) in nums:
            continue
        for index2 in range(len(nums)):
            if index2 == index:
                continue
            if nums[index2] == (target - nums[index]) and not index2 in OurIndicesList:
                OurIndicesList.append(index)
                OurIndicesList.append(index2)
                return OurIndicesList

def twoSum1(self, nums: List[int], target: int) -> List[int]:
    our_dict = dict()
    for index, value in enumerate(nums):
        if (x := (target - value)) in our_dict:
            return [index, our_dict[x]]
        our_dict[value] = index
    return None

list = twoSum([-1,-2,-3,-4,-5], (-8))
print(list)